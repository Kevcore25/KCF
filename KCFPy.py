import ast, json, os

# Version stuff
VERSION = 2.1
VERSION_HIGHLIGHTS = """
2.0 Changes:
+ More MC functions (e.g. setblock, give, effect)
+ Automatic variable declaration
+ Automatic custom commands implementation with triggers
"""

# Turn debug mode on or off
debug = False

def convert_condition_astobj(op: ast.operator):
    """
    Converts an ast object of an operator type (e.g. <) into its string value
    """
    if isinstance(op, ast.Lt): return '<'
    elif isinstance(op, ast.LtE): return '<='
    elif isinstance(op, ast.Gt): return '>'
    elif isinstance(op, ast.GtE): return '>='
    elif isinstance(op, ast.NotEq): return '!='
    elif isinstance(op, ast.Eq): return '='


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
            "onfuncs": f"execute if score @s[tag=onfuncs.player] onfuncs.respawn matches 1 run function {self.namespace}:onrespawn\nexecute if score @s onfuncs.join matches 1.. run function {self.namespace}:onjoin\nexecute if score @s onfuncs.death matches 1.. run function {self.namespace}:ondeath\nexecute unless entity @s[tag=onfuncs.player] run function {self.namespace}:onnewjoin",

            "onjoin": "scoreboard players set @s onfuncs.join 0",
            "ondeath": "scoreboard players set @s onfuncs.death 0",
            "onrespawn": "", # Devs: You can also make your own "while dead" by doing: if self.onfuncs.death == 0:
            "onnewjoin": "tag @s add onfuncs.player",

            "triggers": ""
        }

        self.conditions = 0
        self.precision = 2
        self.variables = {}
        self.triggers = []
        self.pNumbers = []
        self.tempi = 0


    def get_value(self, val) -> str:
        if isinstance(val, ast.Name):
            if val.id.startswith("_"):
                return self.labels[val.id[1:]]
            return val.id
        elif isinstance(val, ast.Constant):
            return val.value
        elif isinstance(val, ast.Attribute):
            return self.get_value(val.value) + "." + val.attr
        
    def get_dict(self, dictionary: ast.Dict) -> dict:
        new = {}

        for i in range(len(dictionary.keys)):
            key = dictionary.keys[i]            
            val = dictionary.values[i]

            if isinstance(val, ast.Dict):
                val = self.get_dict(val)
            else:
                val = self.get_value(val)

            new[key.id] = val

        if debug: print(new)
        return new
        

    def command(self, cmd: str, args: list[ast.Constant, ast.Attribute, ast.Name]) -> str:
        match cmd:
            case "setblock":
                if len(args) == 2:
                    return f"setblock {self.get_value(args[0])} {self.get_value(args[1])}"
                elif len(args) == 3:
                    return f"setblock {self.get_value(args[0])} {self.get_value(args[1])} {args[2].id}"
                
            case "fill":
                if len(args) == 3:
                    return f"fill {self.get_value(args[0])} {self.get_value(args[1])} {self.get_value(args[2])}"
                elif len(args) == 4:
                    return f"fill {self.get_value(args[0])} {self.get_value(args[1])} {self.get_value(args[2])} {args[3].id}"

            case "execute":
                return (f"execute {' '.join(i.value for i in args[:-1])} run function {self.namespace}:{args[-1].id}")
            
            case "effect":
                if len(args) == 2:
                    return f"effect give {self.get_entity(self.get_value(args[0]))} {self.get_value(args[1])}"
                elif len(args) == 3:
                    return f"effect give {self.get_entity(self.get_value(args[0]))} {self.get_value(args[1])} {args[2].value}"
                elif len(args) == 4:
                    return f"effect give {self.get_entity(self.get_value(args[0]))} {self.get_value(args[1])} {args[2].value} {args[3].value}"
                
            case "cleareffect":
                return f"effect clear {self.get_entity(self.get_value(args[0]))} {self.get_value(args[1])}"

            case "give":
                if len(args) == 2:
                    return f"give {self.get_entity(self.get_value(args[0]))} {self.get_value(args[1])} 1"
                elif len(args) == 3:
                    return f"give {self.get_entity(self.get_value(args[0]))} {self.get_value(args[1])} {args[2].value}"
                elif len(args) == 4:
                    components = self.get_dict(args[3])
                    new = []
                    # Due to how MC components work, the first one instead of being : must be =
                    for k, v in components.items():
                        new.append(f"{k}={json.dumps(v)}")

                    return f"give {self.get_entity(self.get_value(args[0]))} {self.get_value(args[1])}[{','.join(new)}] {args[2].value}"
            case "summon":
                if len(args) == 1:
                    return f"summon {self.get_value(args[0])}"
                elif len(args) == 2:
                    return f"summon {self.get_value(args[0])} {self.get_value(args[1])}"
                elif len(args) == 3:
                    return f"summon {self.get_value(args[0])} {self.get_value(args[1])} {self.get_value(args[2])}"

        raise TypeError(f"Function '{cmd}' failed to be parsed.")

    def get_player(self, player: str):
        match player:
            case "all": return "@a"
            case "self": return "@s"
            case "nearest": return "@p"
            case "random": return "@r"
            case _:
                if player.startswith("_"):
                    return self.labels[player[1:]]
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

    def bool_to_if(self, value: bool):
        if value:
            y = "if"
            n = "unless"
        else:
            y = 'unless'
            n = 'if'

        return y, n
    
    def parse_condition(self, condition):
        temp = "execute "
        def cmpre(value, opp=False):
            nonlocal temp

            y, n = self.bool_to_if(not opp)

            if isinstance(value, ast.Compare):                    
                entity, varName = self.parse_var(value.left)

                if isinstance(value.comparators[0], ast.Constant):
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
                    # Detect 
                    if isinstance(value.ops[0], ast.NotEq):
                        temp += f"{n} score {entity} {varName} = {entity2} {varName2} "
                    else:
                        temp += f"{y} score {entity} {varName} {convert_condition_astobj(value.ops[0])} {entity2} {varName2} "

            elif isinstance(value, ast.Call):
                match value.func.id:
                    case "entity":
                        temp += f"{y} entity {self.get_entity(value.args[0].value)} "
                    case "block":
                        temp += f"{y} block {self.get_value(value.args[0])} {self.get_value(value.args[1])} "
                    case "custom":
                        temp += value.args[0].value + " "

            elif isinstance(value, ast.BoolOp):
                if isinstance(value.op, ast.And):
                    for v in value.values:
                        cmpre(v)
                elif isinstance(value.op, ast.Or):
                    for v in value.values:
                        temp += "\n" + self.parse_condition(v)

            elif isinstance(value, ast.Constant):
                if isinstance(value.value, str):
                    temp += f"{y} {value.value} "
                elif value.value == False:
                    # Put a random FALSE statement
                    temp += "unless score 1 p-numbers = 1 p-numbers"
            
        cmpre(condition)

        return temp + "%end%"

    def parse_var(self, expression: ast.Attribute | ast.Name) -> tuple[str, str]:
        if isinstance(expression, ast.Attribute):
            if isinstance(expression.value, ast.Attribute):
                a, b = self.parse_var(expression.value)
                return a, b + "." + expression.attr

            return self.get_entity(self.get_value(expression.value)), expression.attr
        elif isinstance(expression, ast.Name):
            return "#global", expression.id

    def write(self, filename: str, data: str):
        filename = filename.replace("__", "/")
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
            statements, result_expr = convert_binop(expression.value, ".temp", self.tempi)
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
        temp = []

        if isinstance(expression.value, ast.Constant):
            # Must be var, so
            for var in expression.targets:
                # If self, e.g.                    
                # # IF LABEL, aka starts with _:
                if isinstance(var, ast.Name) and var.id.startswith("_"):
                    self.labels[var.id[1:]] = expression.value.value

                else:
                    entity, varName = self.parse_var(var)

                    if varName not in self.variables:
                        self.variables[varName] = "dummy"

                    temp.append(f"scoreboard players set {entity} {varName} {expression.value.value}")
        elif isinstance(expression.value, ast.BinOp):
            # Convert to AugAssign statements
            statements, result_expr = convert_binop(expression.value, ".temp", self.tempi)
            self.tempi += 1

            # Create final assignment
            final_assignment = ast.Assign(
                targets=expression.targets,
                value=result_expr
            )

            # Combine all statements
            all_statements = statements + [final_assignment]

            for ass in all_statements:
                if isinstance(ass, ast.AugAssign):
                    temp.append(self.aug_assign(ass))
                else:
                    temp.append(self.assign(ass))
            
            
        else:
            entity2, varName2 = self.parse_var(expression.value)
            
            for var in expression.targets:
                entity1, varName1 = self.parse_var(var)
                # Add to vars
                self.variables[varName1] = "dummy"

                temp.append(f"scoreboard players operation {entity1} {varName1} = {entity2} {varName2}")

        return "\n".join(temp)

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
            if debug: print(ast.dump(expression))

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
                        funcname = expression.value.func.id
                        funcname = funcname.replace("__", '/')
                        cmds.append(f"function {self.namespace}:{funcname}")
                    else:
                        args = expression.value.args
                        func = expression.value.func.id

                        match func:
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
                            case _:
                                cmd = self.command(func, args)
                                cmds.append(cmd)
                        
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
                    temp = temp.replace("%end%", f"run return run function {self.namespace}:{fname}t")


                    self.write(fname, temp + "\n" + self.parse(expression.orelse, fname))
                    self.write(fname + "t", self.parse(expression.body, fname + "t"))
                
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
            elif isinstance(expression, ast.For):
                fname = f"{filename}_for{self.conditions}"

                # Get the variable name
                var = expression.target.id

                # Add to global vars
                self.variables[var] = "dummy"

                # Get the range
                if isinstance(expression.iter, ast.Call) and expression.iter.func.id == "range":
                    args = expression.iter.args

                    step = 1
                    start = 0
                    if len(args) == 1:
                        end = args[0].value
                    elif len(args) == 2:
                        start = args[0].value
                        end = args[1].value
                    elif len(args) == 3:
                        start = args[0].value
                        end = args[1].value
                        step = args[2].value

                    cmds.append(f"scoreboard players set #global {var} {start}\nfunction {self.namespace}:{fname}")

                    self.write(fname, self.parse(expression.body, fname) +f"\nscoreboard players add #global {var} {step}\nexecute if score #global {var} matches ..{end - 1} run function {self.namespace}:{fname}")
                    
                    self.conditions += 1
        return "\n".join(cmds)
  
    def add_extras(self):
        # ADD VARIABLES
        for var, t in self.variables.items():
            if t == 'dummy':
                v = f"scoreboard objectives add {var} dummy"
                if v not in self.files['load'].splitlines():
                    self.files['load'] = v + "\n" + self.files['load']

        # ADD ALL VARIABLES INTO UNINSTALL FUNCTION
        temp = [f"scoreboard objectives remove {var}" for var, type in self.variables.items()]
        for v in temp:
            if v not in self.files['uninstall'].splitlines():
                self.files['uninstall'] = v + "\n" + self.files['uninstall']

        # ADD TRIGGERS
        if len(self.triggers) > 0:
            self.files['onfuncs'] += f"\nfunction {self.namespace}:triggers"

            for trigger in self.triggers:
                # Add a register
                self.files['triggers'] += f"\nscoreboard players enable @s {trigger}\nexecute if score @s {trigger} matches 1.. at @s run function {self.namespace}:triggers/{trigger}"

                # Create trigger
                if "triggers/" + trigger not in self.files:
                    self.files['triggers/' + trigger] = f"scoreboard players reset @s {trigger}"
                else:
                    self.files['triggers/' + trigger] = self.files['triggers/' + trigger] + f"\nscoreboard players reset @s {trigger}"


        # ADD P NUMS to LOAD
        pNumCmds = "\n".join(f"scoreboard players set {n} .temp {n}" for n in self.pNumbers)

        self.files['load'] = "scoreboard objectives add .temp dummy\nscoreboard objectives add p-numbers dummy\n" + pNumCmds + "\n" + self.files['load']
        

    def build(self):
        self.parse(self.code)
        self.add_extras()

    def write_files(self, destination: str = "."):
        for file, contents in self.files.items():
            files = file.split('/')
            if not os.path.isdir(os.path.join(destination, *files[:-1])):
                os.mkdir(os.path.join(destination, *files[:-1]))
            with open(os.path.join(destination, *files[:-1], files[-1] + ".mcfunction"), 'w') as f:
                f.write(contents)
