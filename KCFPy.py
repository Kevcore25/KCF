import ast, json, os, re

# Version stuff
VERSION = 3.0
VERSION_HIGHLIGHTS = """
3.0 Changes:
* Forced all function names to be lowered
* "Function" type now accepts both a function name, or a function call
* Added FormattedString for title/tellraw commands
* Added a bunch of commonly used commands
"""

# Turn debug mode on or off
debug = True


colors = {
    'red':'red',
    'orange':'gold',
    'yellow':'yellow',
    'green':'green',
    'aqua':'aqua',
    'blue':'blue',
    'dark_blue':'dark_blue',
    'dark_aqua':'dark_aqua',
    'purple':'dark_purple',
    'pink':'light_purple',
    'magenta':'light_purple',
    'black':'black',
    'gray':'gray',
    'grey':'gray',
    'light_gray':'light_gray',
    'light_grey':'light_gray',
    'dark_gray':'dark_gray',
    'dark_grey':'dark_gray',
    'white':'white'
}

def is_hex(s: str):
    return set(s) <= set('0123456789abcdef')

def ktf(formats: str) -> dict:
    result = {}

    for format in formats.split(','):
        format = format.strip()

        if format in ('r', 'reset'):
            result = {'bold': False, "italic": False, "underlined": False, "color": "white", "strikethrough": False, "obfuscated": False}

        elif format in ('b', 'bold'):
            result['bold'] = True
        elif format in ('i', 'italic'):
            result['italic'] = True
        elif format in ('u', 'underline', 'underlined'):
            result['underlined'] = True

        # Use mathematics and SET theory to condense code.
        elif set(format) <= set("biu") and len(format) <= 3 and format != "bbb": # bbb is valid hex
            if 'b' in format: result['bold'] = True
            if 'i' in format: result['italic'] = True
            if 'u' in format: result['underlined'] = True

        ## Colours

        # 3-digit hex
        elif len(format) == 3 and is_hex(format):
            temp = ""
            for i in format:
                temp += i * 2
            result['color'] = '#' + temp
        elif len(format) == 6 and is_hex(format):
            result['color'] = '#' + format

        elif format in list(colors):
            result['color'] = colors[format]

    return result

def textformat(cmd: str): 

    ft = lambda txt: re.findall(r"#([^#]*)#",txt)

    def ms(text, color="", b=None, i=None, u=None):
        s = {"text": text}

        if color != "":
            s["color"] = color
        if b is not None:
            s["bold"] = b
        if i is not None:
            s["italic"] = i
        if u is not None:
            s["underlined"] = u


        return s

    c = ""
    b,i,u = None,None,None

    l = []

    if "#" in cmd and not cmd.startswith("#"): l.append(cmd.split("#")[0])

    for _ in range(100): # Only allow a certain amount of executions
        a = ft(cmd)
        if len(a) > 0:
            t = a[0]
            for tag in t.split(","):
                tag = tag.lower()
                if tag in ["b","bold"]: b = True
                elif tag in ["i","italic"]: i = True
                elif tag in ["u","underlined"]: u = True

                # Detect bi bu stuff
                elif set(tag) <= set("biu") and len(tag) <= 3 and tag != "bbb":
                    if 'b' in tag: b = True
                    if 'i' in tag: i = True
                    if 'u' in tag: u = True

                # If a vaild color is specified, change the color
                elif tag in list(colors):
                    c = colors[tag]
                # RGB hex
                elif set(tag) <= set("0123456789abcdef") and (len(tag) == 6 or len(tag) == 3):
                    if len(tag) == 6: c = "#" + tag
                    else: 
                        c = "#"
                        for letter in tag:
                            c += letter+letter

                # Reset
                elif tag in ["r","reset"]:
                    c = "white"
                    b,i,u = False,False,False


            cmd = cmd.split(f"#{t}#",1)[1]      

        
        if "#" in cmd: txt = cmd.split("#")[0]
        else: txt = cmd
        l.append(ms(txt, c, b,i,u))
        if "#" not in cmd: break

    return l

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

    elif isinstance(op, ast.Add): return '+'
    elif isinstance(op, ast.Sub): return '-'
    elif isinstance(op, ast.Mult): return '*'
    elif isinstance(op, ast.Div) or isinstance(op, ast.FloorDiv): return '/'
    elif isinstance(op, ast.Mod): return '%'

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
    temp_store = ast.Attribute(value=ast.Name(id=f'.t{tempi}', ctx=ast.Store()), attr=temp_name, ctx=ast.Store())
    temp_load = ast.Attribute(value=ast.Name(id=f'.t{tempi}', ctx=ast.Load()), attr=temp_name, ctx=ast.Load())

    # Generate statements
    statements = [
        ast.Assign(targets=[temp_store], value=operands[0])
    ]
    
    for operand in operands[1:]:
        if isinstance(operand, ast.Constant):
            statements.append(
                ast.AugAssign(target=temp_store, op=binop_node.op, value=operand)
            )
        else:
            statements.append(
                ast.AugAssign(target=operand, op=binop_node.op, value=temp_store)
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

        self.precision = 3

        # PRESET CODE
        self.files = {
            # Typical functions
            "load": "scoreboard objectives add onfuncs.join custom:leave_game\nscoreboard objectives add onfuncs.death deathCount\nscoreboard objectives add onfuncs.respawn custom:time_since_death",
            "tick": f"execute as @a run function {self.namespace}:onfuncs",
            "uninstall": "scoreboard objectives remove .temp\nscoreboard objectives remove p-numbers",
            
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

    def fstring(self, text: ast.JoinedStr | ast.Constant) -> str:
        result = []

        # Firstly, determine is the text is even a JOINED STR
        if isinstance(text, ast.JoinedStr):
            for value in text.values:
                if isinstance(value, ast.Constant):
                    result += textformat(value.value)
                elif isinstance(value, ast.FormattedValue):

                    if value.format_spec is not None:
                        t: str = value.format_spec.values[0].value.strip()
                        c = None

                        # Specified colour / formatting
                        if "|" in t:
                            t, c = t.split("|", 1)
                            t = t.strip()
                            c = c.strip()

                        temp = {}

                        # Match type
                        match t:
                            case "var" | "score" | "": # Empty = not specified = var
                                entity, varName = self.parse_var(value.value)
                                temp = {"score": {"objective": varName, "name": entity}}
                            case "entity" | "player" | "selector":
                                temp = {"selector": self.get_entity(self.get_value(value.value))}

                        # Apply colour
                        if c is not None:
                            temp |= ktf(c) # |= is valid?

                        result.append(temp)
                    else:
                        entity, varName = self.parse_var(value.value)
                        result.append({"score": {"objective": varName, "name": entity}})

            return result
        
        # Otherwise if it is a constant
        elif isinstance(text, ast.Constant):
            return text.value
        
        else:
            return ""

    def get_func(self, function: ast.Name | ast.Lambda, filename: str = ""):
        if isinstance(function, ast.Name):
            return f"function {self.namespace}:{function.id}" 
        elif isinstance(function, ast.Lambda):                
            fname = filename + f'_lmb{self.conditions}'
            self.conditions += 1

            code = self.parse([ast.Expr(value=function.body)], fname)
            if code.count('\n') == 0:
                return code
            else:
                self.write(fname, code)
                return f"function {self.namespace}:{fname}"
        elif isinstance(function, ast.Call):
            fname = filename + f'_lmb{self.conditions}'
            self.conditions += 1

            code = self.parse([ast.Expr(value=function)], fname)
            if code.count("\n") == 0:
                return code
            else:
                self.write(fname, code)
                return f"function {self.namespace}:{fname}"

        raise TypeError("Not a valid function")
    
    def get_int(self, value: ast.Constant | ast.UnaryOp):
        # If it is negative it is a unary op for some reason
        if isinstance(value, ast.UnaryOp) and isinstance(value.op, ast.USub):
            return -value.operand.value
        else:
            return value.value

    def command(self, cmd: str, args: list[ast.Constant, ast.Attribute, ast.Name], filename: str = "") -> str:
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
                return (f"execute {' '.join(i.value for i in args[:-1])} run {self.get_func(args[-1], filename)}")
            
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

            case "attribute":
                if len(args) == 2:
                    return f"attribute {self.get_entity(self.get_value(args[0]))} {self.get_value(args[1])} base get"
                elif len(args) == 3:
                    return f"attribute {self.get_entity(self.get_value(args[0]))} {self.get_value(args[1])} base set {self.get_int(args[2])}"
            case "resetattribute":
                return f"attribute {self.get_entity(self.get_value(args[0]))} {self.get_value(args[1])} base reset"

            # CREATORS: Just use the RUN function for now.
            # case "bossbar":
            #     match self.get_value(args[0]).lower():
            #         case "add" | "create":
            #             return f"bossbar add {self.}"

            case "dialog":
                if len(args) == 1:
                    return f"dialog clear {self.get_player(args[0])}"
                elif len(args) == 2:
                    return f"dialog show {self.get_player(args[0])}{self.get_value(args[1])}"
                
            case "enchant":
                if len(args) == 2:
                    return f"enchant {self.get_player(args[0])} {self.get_value(args[1])}"
                elif len(args) == 3:
                    return f"enchant {self.get_player(args[0])} {self.get_value(args[1])} {args[2].value}"
            
            case "kill":
                return f"kill {self.get_entity(self.get_value(args[0]))}"
            
            case "getplayers":
                player, name = self.parse_var(args[0])
                return f"scoreboard players reset {player} {name}\nexecute at @a run scoreboard players add {player} {name} 1"
            
            case "randint":
                player, name = self.parse_var(args[0])

                return f"execute store result score {player} {name} run random value {self.get_int(args[1])}..{self.get_int(args[2])}"

            case "tellraw":
                return f"tellraw {self.get_player(self.get_value(args[0]))} {json.dumps(self.fstring(args[1]))}"
            
            case "title":
                return f"title {self.get_player(self.get_value(args[0]))} title {json.dumps(self.fstring(args[1]))}"
            case "subtitle":
                return f"title {self.get_player(self.get_value(args[0]))} subtitle {json.dumps(self.fstring(args[1]))}"
            case "times":
                if len(args) == 4:
                    return f"title {self.get_player(self.get_value(args[0]))} times {args[1].value} {args[2].value} {args[3].value}"
                elif len(args) == 2:
                    return f"title {self.get_player(self.get_value(args[0]))} times {args[1].value}"
               
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
    
    def parse_condition(self, condition, starting = 'execute '):
        temp = starting
        add = True
        def cmpre(value, opp=False):
            nonlocal temp, add

            y, n = self.bool_to_if(not opp)

            if isinstance(value, ast.Compare):                    
                entity, varName = self.parse_var(value.left)

                if isinstance(value.comparators[0], ast.Constant) or isinstance(value.comparators[0], ast.UnaryOp):
                    if isinstance(value.ops[0], ast.Eq):
                        temp += (f"{y} score {entity} {varName} matches {self.get_int(value.comparators[0])} ")
                    elif isinstance(value.ops[0], ast.NotEq):
                        temp += (f"{n} score {entity} {varName} matches {self.get_int(value.comparators[0])} ")
                    elif isinstance(value.ops[0], ast.Gt):
                        temp += (f"{y} score {entity} {varName} matches {self.get_int(value.comparators[0]) + 1}.. ")
                    elif isinstance(value.ops[0], ast.GtE):
                        temp += (f"{y} score {entity} {varName} matches {self.get_int(value.comparators[0])}.. ")
                    elif isinstance(value.ops[0], ast.Lt):
                        temp += (f"{y} score {entity} {varName} matches ..{self.get_int(value.comparators[0]) - 1} ")
                    elif isinstance(value.ops[0], ast.LtE):
                        temp += (f"{y} score {entity} {varName} matches ..{self.get_int(value.comparators[0])} ")
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
                    print('a', value.values)
                    temp += 'run '
                    t = []
                    for v in value.values:
                        t.append(self.parse_condition(v))
                    temp += f'\n{temp}'.join(t)
                    add = False
            elif isinstance(value, ast.Constant):
                if isinstance(value.value, str):
                    temp += f"{y} {value.value} "
                elif value.value == False:
                    # Put a random FALSE statement
                    temp += "unless score 1 p-numbers = 1 p-numbers"
            
        cmpre(condition)

        print('RESULT', temp)
        if add:
            return temp + "%end%"
        else:
            return temp.replace("execute run ", '')
        
    def parse_var(self, expression: ast.Attribute | ast.Name) -> tuple[str, str]:
        if isinstance(expression, ast.Attribute):
            if isinstance(expression.value, ast.Attribute):
                a, b = self.parse_var(expression.value)
                return a, b + "." + expression.attr

            return self.get_entity(self.get_value(expression.value)), expression.attr
        elif isinstance(expression, ast.Name):
            return "#global", expression.id

    def write(self, filename: str, data: str):
        filename = filename.replace("__", "/").lower()
        if filename not in self.files:
            self.files[filename] = data
        else:
            self.files[filename] += "\n" + data

    def print(self):
        for file in self.files:
            print(f"\nIN FILE {file}.mcfunction:\n" + self.files[file])

    def aug_assign(self, expression: ast.Attribute | ast.Name):
        if isinstance(expression.value, ast.Constant) or isinstance(expression.value, ast.UnaryOp):
            # Must be var, so
            var = expression.target
            # If self, e.g.
            entity, varName = self.parse_var(var)

            value = self.get_int(expression.value)

            if isinstance(expression.op, ast.Add):
                return (f"scoreboard players add {entity} {varName} {value}")
            elif isinstance(expression.op, ast.Sub):
                return (f"scoreboard players remove {entity} {varName} {value}")
            else:

                if isinstance(expression.op, ast.Mult) or isinstance(expression.op, ast.Div) or isinstance(expression.op, ast.FloorDiv):
                    # For decimals, use 2 commands to essnetially give a best rounded answer.
                    if isinstance(value, float):
                        value = expression.value.value

                        # Num of digits after .
                        digits = len(str(value).split('.')[1])

                        if digits > self.precision:
                            precision = self.precision
                        else:
                            precision = digits

                        rvalue = round(value * (10 ** precision))
                        
                        if isinstance(expression.op, ast.Mult):
                            a, b = '*', '/'
                        else:
                            a, b = '/', '*'

                        for i in (rvalue, 10**precision):
                            if i not in self.pNumbers:
                                self.pNumbers.append(i) 
                        return (
                            f"scoreboard players operation {entity} {varName} {a}= {rvalue} p-numbers\n" + 
                            f"scoreboard players operation {entity} {varName} {b}= {10 ** precision} p-numbers" 
                        )
                    else:
                        if value not in self.pNumbers:
                            self.pNumbers.append(value)
                        return (f"scoreboard players operation {entity} {varName} {convert_condition_astobj(expression.op)}= {value} p-numbers")

                elif isinstance(expression.op, ast.Mod):
                    return (f"scoreboard players operation {entity} {varName} %= {value} p-numbers")
            
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

        if isinstance(expression.value, ast.Constant) or isinstance(expression.value, ast.UnaryOp):
            # Must be var, so
            for var in expression.targets:
                # If self, e.g.                    
                # # IF LABEL, aka starts with _:
                if isinstance(var, ast.Name) and var.id.startswith("_"):
                    self.labels[var.id[1:]] = self.get_int(expression.value)

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

            if isinstance(value.right, ast.Constant) or isinstance(value.right, ast.UnaryOp):
                # Must be var, so
                var = value.left
                # If self, e.g.
                entity, varName = self.parse_var(var)


                if isinstance(expression.op, ast.Add):
                    temp.append (f"scoreboard players add {entity} {varName} {self.get_int(expression.right)}")
                elif isinstance(expression.op, ast.Sub):
                    temp.append (f"scoreboard players remove {entity} {varName} {self.get_int(expression.right)}")
                else:
                    if self.get_int(expression.right) not in self.pNumbers:
                        self.pNumbers.append(self.get_int(expression.right))
                    elif isinstance(expression.op, ast.Mult):
                        temp.append (f"scoreboard players operation {entity} {varName} *= {self.get_int(expression.right)} p-numbers")
                    elif isinstance(expression.op, ast.Div) or isinstance(expression.op, ast.FloorDiv):
                        temp.append (f"scoreboard players operation {entity} {varName} /= {self.get_int(expression.right)} p-numbers")
                    elif isinstance(expression.op, ast.Mod):
                        temp.append (f"scoreboard players operation {entity} {varName} %= {self.get_int(expression.right)} p-numbers")
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
    
    def ifexpr(self, expression: ast.If, filename: str):
        condition = self.parse_condition(expression.test)               
        
        # Multiple ifs can get janky: if0_if0_if0.... 
        if '_if' in filename:
            temp = ''
            for i in range(0, len(filename), -1):
                t = filename[i]
                if t.isdigit():
                    temp += t
                else:
                    fname = f"{filename.replace(f'_if{temp}'), f'_if{int(temp) + 1}'}"
            else:
                fname = f"{filename}_if{self.conditions}"
        else:
            fname = f"{filename}_if{self.conditions}"
    
        # Add one if to counter
        self.conditions += 1

        # Expression 
        if isinstance(expression.orelse, ast.Call):
            condition = condition.replace("%end%", f"run function {self.namespace}:{fname}")

            self.write(fname, self.parse([ast.Expr(value=expression.body)], fname))            
            
            return (condition)

        # If not complex (not IF ELSE)
        elif len(expression.orelse) == 0:
            code = self.parse(expression.body, fname)

            # Optimize: If it is only one statement, don't create a new file
            if code.count('\n') == 0:
                condition = condition.replace("%end%", "run " + code)
            else:
                condition = condition.replace("%end%", f"run function {self.namespace}:{fname}")
                self.write(fname, self.parse(expression.body, fname))            
                
            return condition

        else:
            # Use multiple files. 

            # In new file, return if true. If it doesn't run, then the else statement is ran (other function runs)
            # Minimize file usage by APPENDING using write function. 
            # Because, if IF statement runs, the function returns, so code can be directly appended below the if statement

            body = self.parse(expression.body, fname + "t")

            # Do not write if only one line
            if body.count("\n") == 0:
                condition = condition.replace("%end%", f"run return run {body}")
            else:
                condition = condition.replace("%end%", f"run return run function {self.namespace}:{fname}t")
                self.write(fname + "t", body)

            self.write(fname, condition + "\n" + self.parse(expression.orelse, fname))

            return (f"function {self.namespace}:{fname}")
    

    def parse(self, parsed: list[ast.FunctionDef], filename = ""):
        cmds = []

        for expression in parsed:
            if debug: print(ast.dump(expression))

            if isinstance(expression, ast.FunctionDef):
                self.write(expression.name, self.parse(expression.body, expression.name.lower()))
                
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
                        funcname = expression.value.func.id.lower()
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
                                cmd = self.command(func, args, filename)
                                cmds.append(cmd)
                # IF
                elif isinstance(expression.value, ast.IfExp):
                    cmds.append(self.ifexpr(expression.value, filename))
            elif isinstance(expression, ast.If):
                cmds.append(self.ifexpr(expression, filename))
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
            if t == 'dummy' and var != '.temp':
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
        pNumCmds = "\n".join(f"scoreboard players set {n} p-numbers {n}" for n in self.pNumbers)

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
