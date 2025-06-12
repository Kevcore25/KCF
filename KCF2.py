import ast, json, os

def convert_binop(binop_node, temp_name, tempi = 0):
    """
    Converts a compound BinOp node into a list of AugAssign statements
    """

    # Check if operator is supported
    if type(binop_node.op) not in [ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod]:
        return [], binop_node

    def flatten(node, op_type):
        if isinstance(node, ast.BinOp) and type(node.op) is op_type:
            return flatten(node.left, op_type) + [node.right]
        return [node]

    operands = flatten(binop_node, type(binop_node.op))
    
    if len(operands) < 2:
        return [], binop_node

    # Create temporary variable nodes
    temp_store = ast.Attribute(value=ast.Name(id=f'temp{tempi}', ctx=ast.Store()), attr=temp_name, ctx=ast.Store())
    temp_load = ast.Attribute(value=ast.Name(id=f'temp{tempi}', ctx=ast.Load()), attr=temp_name, ctx=ast.Load())

    # Generate statements
    statements = [
        ast.Assign(targets=[temp_store], value=operands[0])
    ]
    
    for operand in operands[1:]:
        statements.append(
            ast.AugAssign(target=temp_store, op=binop_node.op, value=operand)
        )
    
    return statements, temp_load


class KCF:
    """
    Converts parsed KCF into a list of MCFunction files
    """
    
    def __init__(self, code: str):
        self.code = code

        self.labels = {}

        self.namespace = 'kcf'

        # PRESET CODE
        self.files = {
            # Typical functions
            "load": "scoreboard objectives add onfuncs.join custom:leave_game\nscoreboard objectives add onfuncs.death deathCount\nscoreboard objectives add onfuncs.respawn custom:time_since_death",
            "tick": f"execute as @a run function {self.namespace}:onfuncs",
            "uninstall": "",
            
            # On action functions        
            "onfuncs": f"execute if score @s onfuncs.join matches 1.. run function {self.namespace}:onjoin\nexecute if score @s onfuncs.death matches 1.. run function {self.namespace}:ondeath\nexecute if score @s onfuncs.respawn matches 1.. run function {self.namespace}:onrespawn\nexecute unless entity @s[tag=onfuncs.player] run function {self.namespace}:onnewjoin",

            "onjoin": "scoreboard players set @s onfuncs.join 0",
            "ondeath": "scoreboard players set @s onfuncs.death 0",
            "onrespawn": "scoreboard players set @s onfuncs.respawn 0",
            "onnewjoin": "tag @s add onfuncs.player"
        }

        self.conditions = 0
        self.precision = 2
        self.variables = {}
        self.triggers = []
        self.pNumbers = []
        self.tempi = 0

    def get_player(self, player: str):
        match player:
            case "all": return "@a"
            case "self": return "@s"
            case "nearest": return "@p"
            case "random": return "@r"
            case _:
                if player.startswith("#"):
                    return self. labels[player[1:]]
                return player
            
    def get_entity(self, entity: str):
        match entity:
            case "all": return "@a"
            case "self": return "@s"
            case "nearest": return "@n"
            case "randomplayer": return "@r"
            case "nearestplayer": return "@r"
            case "every": return "@e"
            case _:
                if entity.startswith("_"):
                    try:
                        return self.labels[entity[1:]]
                    except KeyError:
                        raise NameError("Label is not found!")
                return entity

    def parse_get_var(self, var: str):
        if "." in var:
            entity, varname = var.split('.', 2)
            return [self.get_entity(entity), varname]
        elif var.isdigit():
            if var not in self.pNumbers:
                self.pNumbers.append(var)
            return ['p-numbers', var]
        else:
            return ['#global', var]

    def parse_message(self, message: str):
        msg = []

        while ("${" in message):
            plain, vart = message.split("${", 1)
            msg.append(plain)

            varmsg = vart.split("}")[0]

            var = self.parse_get_var(varmsg)

            msg.append({"score": {"name": var[0], "objective": var[1]}})

            message = message.split("}", 1)[1]
        
        msg.append(message)
        
        if msg[-1] == "":
            msg.pop()

        return json.dumps(msg)


    def parse_condition(self, condition):
        temp = "execute "
        def cmpre(value, opp=False):
            nonlocal temp

            if not opp:
                y = "if"
                n = "unless"
            else:
                y = 'unless'
                n = 'if'

            if isinstance(value, ast.Compare):
                if isinstance(value.comparators[0], ast.Constant):
                    entity, varName = self.parse_var(value.left)
                    if isinstance(value.ops[0], ast.Eq):
                        temp += (f"{y} score {entity} {varName} matches {value.comparators[0].value} ")
                    elif isinstance(value.ops[0], ast.NotEq):
                        temp += (f"{n} score {entity} {varName} matches {value.comparators[0].value} ")
                    elif isinstance(value.ops[0], ast.Gt):
                        temp += (f"{y} score {entity} {varName} matches {value.comparators[0].value + 1}.. ")
                    elif isinstance(value.ops[0], ast.GtE):
                        temp += (f"{y} score {entity} {varName} matches {value.comparators[0].value}.. ")
                    elif isinstance(value.ops[0], ast.Lt):
                        temp += (f"{y} score {entity} {varName} matches ..{value.comparators[0].value - 1} ")
                    elif isinstance(value.ops[0], ast.LtE):
                        temp += (f"{y} score {entity} {varName} matches ..{value.comparators[0].value} ")
                else:
                    entity2, varName2 = self.parse_var(value.comparators[0])
                    temp += (f"{y} score {entity} {varName} = {entity2} {varName2} ")
            elif isinstance(value, ast.Call):
                match value.func.id:
                    case "entity":
                        temp += f"{y} entity {self.get_entity(value.args[0].value)} "
                    case "block":
                        temp += f"{y} block {self.get_entity(' '.join(i.value for i in value.args))} "
                    case "custom":
                        temp += value.args[0].value + " "
            elif isinstance(value, ast.BoolOp):
                if isinstance(value.op, ast.And):
                    for v in value.values:
                        cmpre(v)
                elif isinstance(value.op, ast.Or):
                    for v in value.values:
                        temp += "\n" + self.parse_condition(v)

        cmpre(condition)

        return temp + "%end%"

    def parse_var(self, expression: ast.Attribute | ast.Name) -> tuple[str, str]:
        if isinstance(expression, ast.Attribute):
            return self.get_entity(expression.value.id), expression.attr
        elif isinstance(expression, ast.Name):
            return "#global", expression.id

    def write(self, filename: str, data: str):
        if filename not in self.files:
            self.files[filename] = data
        else:
            self.files[filename] += "\n" + data

    def print(self):
        for file in self.files:
            print(f"\nIN FILE {file}.mcfunction:\n" + self.files[file])

    def aug_assign(self, expression: ast.Attribute | ast.Name):
        if isinstance(expression.value, ast.Constant):
            # Must be var, so
            var = expression.target
            # If self, e.g.
            entity, varName = self.parse_var(var)

            if isinstance(expression.op, ast.Add):
                return (f"scoreboard players add {entity} {varName} {expression.value.value}")
            elif isinstance(expression.op, ast.Sub):
                return (f"scoreboard players remove {entity} {varName} {expression.value.value}")
            else:
                if expression.value.value not in self.pNumbers:
                    self.pNumbers.append(expression.value.value)
                if isinstance(expression.op, ast.Mult):
                    return (f"scoreboard players operation {entity} {varName} *= {expression.value.value} p-numbers")
                elif isinstance(expression.op, ast.Div) or isinstance(expression.op, ast.FloorDiv):
                    return (f"scoreboard players operation {entity} {varName} /= {expression.value.value} p-numbers")
                elif isinstance(expression.op, ast.Mod):
                    return (f"scoreboard players operation {entity} {varName} %= {expression.value.value} p-numbers")
            
        elif isinstance(expression.value, ast.BinOp):
            # cmds.extend(self.create_simp_var(expression.value))
            # Convert to AugAssign statements
            statements, result_expr = convert_binop(expression.value, "temp", self.tempi)
            self.tempi += 1

            # Create final assignment
            final_assignment = ast.AugAssign(
                target=result_expr,
                op=expression.op,
                value=expression.target
            )

            # Combine all statements
            all_statements = statements + [final_assignment]

            temp = []

            for ass in all_statements:

                if isinstance(ass, ast.AugAssign):
                    temp.append(self.aug_assign(ass))
                else:
                    temp.append(self.assign(ass))
            
            return "\n".join(temp)
        else:
            entity, varName = self.parse_var(expression.value)
            
            var = expression.target

            entity1, varName1 = self.parse_var(var)

            if isinstance(expression.op, ast.Add):
                return (f"scoreboard players operation {entity} {varName} += {entity1} {varName1}")
            elif isinstance(expression.op, ast.Sub):
                return (f"scoreboard players operation {entity} {varName} -= {entity1} {varName1}")
            elif isinstance(expression.op, ast.Mult):
                return (f"scoreboard players operation {entity} {varName} *= {entity1} {varName1}")
            elif isinstance(expression.op, ast.Div) or isinstance(expression.op, ast.FloorDiv):
                return (f"scoreboard players operation {entity} {varName} /= {entity1} {varName1}")
            elif isinstance(expression.op, ast.Mod):
                return (f"scoreboard players operation {entity} {varName} %= {entity1} {varName1}")

    def assign(self, expression: ast.Assign):
        # Constant
        if isinstance(expression.value, ast.Constant):
            # Must be var, so
            for var in expression.targets:
                # If self, e.g.                    
                # # IF LABEL, aka starts with _:
                if isinstance(var, ast.Name) and var.id.startswith("_"):
                    self.labels[var.id[1:]] = expression.value.value

                else:
                    entity, varName = self.parse_var(var)

                    return (f"scoreboard players set {entity} {varName} {expression.value.value}")
        elif isinstance(expression.value, ast.BinOp):
            # cmds.extend(self.create_simp_var(expression.value))
            # Convert to AugAssign statements
            statements, result_expr = convert_binop(expression.value, "temp", self.tempi)
            self.tempi += 1

            # Create final assignment
            final_assignment = ast.Assign(
                targets=expression.targets,
                value=result_expr
            )

            # Combine all statements
            all_statements = statements + [final_assignment]

            temp = []

            for ass in all_statements:
                if isinstance(ass, ast.AugAssign):
                    temp.append(self.aug_assign(ass))
                else:
                    temp.append(self.assign(ass))
            
            return "\n".join(temp)
            
        else:
            entity2, varName2 = self.parse_var(expression.value)
            
            for var in expression.targets:
                entity1, varName1 = self.parse_var(var)

                return (f"scoreboard players operation {entity1} {varName1} = {entity2} {varName2}")

    def create_simp_var(self, value: ast.BinOp, times = 0):
        temp = []

        value.left # Left Side of expression
        value.right # Farest Side of Expression, which is VAR (e.g. 10 or self.x)

        if isinstance(value.left, ast.BinOp):
            temp.extend(self.create_simp_var(value.left, times + 1))
        else:                
            expression = value

            if isinstance(value.right, ast.Constant):
                # Must be var, so
                var = value.left
                # If self, e.g.
                entity, varName = self.parse_var(var)


                if isinstance(expression.op, ast.Add):
                    temp.append (f"scoreboard players add {entity} {varName} {expression.right.value}")
                elif isinstance(expression.op, ast.Sub):
                    temp.append (f"scoreboard players remove {entity} {varName} {expression.right.value}")
                else:
                    if expression.right.value not in self.pNumbers:
                        self.pNumbers.append(expression.right.value)
                    elif isinstance(expression.op, ast.Mult):
                        temp.append (f"scoreboard players operation {entity} {varName} *= {expression.right.value} p-numbers")
                    elif isinstance(expression.op, ast.Div) or isinstance(expression.op, ast.FloorDiv):
                        temp.append (f"scoreboard players operation {entity} {varName} /= {expression.right.value} p-numbers")
                    elif isinstance(expression.op, ast.Mod):
                        temp.append (f"scoreboard players operation {entity} {varName} %= {expression.right.value} p-numbers")
            else:
                entity, varName = self.parse_var(expression.right)
                
                var = expression.target

                entity1, varName1 = self.parse_var(var)

                if isinstance(expression.op, ast.Add):
                    temp.append (f"scoreboard players operation {entity} {varName} += {entity1} {varName1}")
                elif isinstance(expression.op, ast.Sub):
                    temp.append (f"scoreboard players operation {entity} {varName} -= {entity1} {varName1}")
                elif isinstance(expression.op, ast.Mult):
                    temp.append (f"scoreboard players operation {entity} {varName} *= {entity1} {varName1}")
                elif isinstance(expression.op, ast.Div) or isinstance(expression.op, ast.FloorDiv):
                    temp.append (f"scoreboard players operation {entity} {varName} /= {entity1} {varName1}")
                elif isinstance(expression.op, ast.Mod):
                    temp.append (f"scoreboard players operation {entity} {varName} %= {entity1} {varName1}")
        return temp
    
    def parse(self, parsed: list[ast.FunctionDef], filename = ""):
        cmds = []

        for expression in parsed:

            if isinstance(expression, ast.FunctionDef):
                self.write(expression.name, self.parse(expression.body, expression.name))
                
            elif isinstance(expression, ast.Assign):
                cmds.append(self.assign(expression))

            elif isinstance(expression, ast.AugAssign):
                # Constant
                cmds.append(
                    self.aug_assign(expression)
                )

            elif isinstance(expression, ast.Expr):
                # This is hard; it is a generic expression

                # Function
                if isinstance(expression.value, ast.Call):
                    # IF THERE ARE NO ARGUMENTS, run USER defined function, otherwise run built-in

                    if len(expression.value.args) == 0:
                        cmds.append(f"function {self.namespace}:{expression.value.func.id}")
                    else:
                        args = expression.value.args
                        func = expression.value.func.id

                        match func:
                            case "execute":
                                cmds.append(f"execute {' '.join(i.value for i in args[:-1])} run function {self.namespace}:{args[-1].id}")
                            case "run":
                                cmds.append(args[0].value)
                            case "var":
                                if len(args) == 1:
                                    vartype = "dummy"
                                elif len(args) == 2:
                                    vartype = args[1].value
                                    if vartype == 'int':
                                        vartype = "dummy"
                                cmds.append(f"scoreboard objectives add {args[0].value} {vartype}")
                                self.variables[args[0].value] = vartype
                            case "trigger":
                                cmds.append(f"scoreboard objectives add {args[0].value} trigger")
                                self.triggers.append(args[0].value)
                            case "label":
                                self.labels[args[0].value] = args[1].value
                        
            elif isinstance(expression, ast.If):
                temp = self.parse_condition(expression.test)               
                
                fname = f"{filename}_if{self.conditions}"
                
                # If not complex (not IF ELSE)
                if len(expression.orelse) == 0:

                    temp = temp.replace("%end%", f"run function {self.namespace}:{fname}")
                    cmds.append(temp)

                    self.write(fname, self.parse(expression.body, fname))
                else:
                    # Use multiple files. 
                    cmds.append(f"function {self.namespace}:{fname}")

                    # In new file, return if true. If it doesn't run, then the else statement is ran (other function runs)
                    # Minimize file usage by APPENDING using write function. 
                    # Because, if IF statement runs, the function returns, so code can be directly appended below the if statement
                    temp = temp.replace("%end%", f"run return run function {self.namespace}:{fname}T")


                    self.write(fname, temp + "\n" + self.parse(expression.orelse, fname))
                    self.write(fname + "T", self.parse(expression.body, fname + "T"))
                
                # Add one if to counter
                self.conditions += 1
            elif isinstance(expression, ast.While):
                # NOTICE: WHILE..ELSE does NOT WORK, and will NOT be planned to be made anytime soon

                # In a while loop, do this:
                # function kcf:file_while0
                # In file_while0:
                # // CODE
                # execute if condition run function kcf:file_while

                # Run the initial compare
                temp = self.parse_condition(expression.test)                    
                
                fname = f"{filename}_while{self.conditions}"
            
                # Use multiple files. 
                cmds.append(f"function {self.namespace}:{fname}")

                temp = temp.replace("%end%", f"run function {self.namespace}:{fname}")

                self.write(fname, self.parse(expression.body, fname) + "\n" + temp)
                
                # Add 1 to the condition counter
                self.conditions += 1

        return "\n".join(cmds)
  
    def add_extras(self):
        # ADD P NUMS to LOAD
        pNumCmds = "\n".join(f"scoreboard players set {n} p-numbers {n}" for n in self.pNumbers)

        self.files['load'] = "scoreboard objectives add temp dummy\nscoreboard objectives add p-numbers dummy\n" + pNumCmds + "\n" + self.files['load']

    def build(self):
        self.parse(self.code)
        self.add_extras()

    def write_files(self, destination: str = "."):
        for file, contents in self.files.items():
            with open(os.path.join(destination, file + ".mcfunction"), 'w') as f:
                f.write(contents)
