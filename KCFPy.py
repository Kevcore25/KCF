import ast, json, os, re

# Version stuff
VERSION = 5.0
VERSION_HIGHLIGHTS = """
NOTE: This is a development version of 5.0!
"""

# Turn debug mode on or off
debug = False

colors = {
    'red':'red',
    'orange':'gold',
    'gold':'gold',
    'yellow':'yellow',
    'green':'green',
    'aqua':'aqua',
    'blue':'blue',
    'dark_blue':'dark_blue',
    'dark_aqua':'dark_aqua',
    'dark_purple':'dark_purple',
    'purple':'dark_purple',
    'pink':'light_purple',
    'magenta':'light_purple',
    'light_purple':'light_purple',
    'black':'black',
    'gray':'gray',
    'grey':'gray',
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
    statements = []
    
    # Process 1st op (might be a nested BinOp)
    if isinstance(operands[0], ast.BinOp):
        nested_statements, nested_result = convert_binop(operands[0], temp_name, tempi + 1)
        statements += nested_statements
        statements.append(ast.Assign(targets=[temp_store], value=nested_result))
    else:
        statements.append(ast.Assign(targets=[temp_store], value=operands[0]))
    
    # Process remaining ops
    for operand in operands[1:]:
        if isinstance(operand, ast.BinOp):
            # Recursively process nested BinOp
            nested_statements, nested_result = convert_binop(operand, temp_name, tempi + 1)
            statements += nested_statements
            statements.append(
                ast.AugAssign(target=temp_store, op=binop_node.op, value=nested_result)
            )
        else:
            statements.append(
                ast.AugAssign(target=temp_store, op=binop_node.op, value=operand)
            )

    if debug:
        for i in statements:
            print('binop', ast.dump(i))

    return statements, temp_load


class KCF:
    """
    Converts parsed KCF into a list of MCFunction files
    """
    
    def __init__(self, code: str):
        self.code = code

        self.labels = {}

        self.namespace = 'kcf'

        self.warnings = []

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

        self.ERROR_THRESHOLD = 1

    def get_lim_num(self, value: ast.Constant, min: int | None = -2147483647, max: int | None = 2147483647) -> int | float:
        """
        Get an int OR float value within bounds.
        """
        if isinstance(value, ast.UnaryOp) or isinstance(value.value, int):
            num = self.get_int(value)
        elif isinstance(value.value, float):
            num = value.value
        else:
            self.raise_error(None, f"Value is not a number!", ast.unparse(value))
            num = value.value

        if (min is not None and max is not None) and not (min <= num <= max):
            self.raise_error(None, f"Number must be between {min} and {max}!", ast.unparse(value), 1)
        elif min is None and not num <= max:
            self.raise_error(None, f"Number must be less than or equal to {max}!", ast.unparse(value), 1)
        elif max is None and not min <= num:
            self.raise_error(None, f"Number must be more than or equal to {min}!", ast.unparse(value), 1)

        return num

    def parse_list(self, value: ast.List) -> str:
        """
        Parses a list and returns it as a String representation
        """
        result = []

        for v in value.elts:
            result.append(str(self.get_abs_value(v)))
        
        # Could just use ', ' for cleaner look?
        return '[' + ','.join(result) + ']'

    def get_abs_value(self, value: ast.Constant | ast.Name | ast.Attribute | ast.List | ast.Dict):
        """
        Returns a representation of a valid MC value.
        The difference between this and get_value is that it accepts more than just String and variables.

        Currently supports all constants (String/float/int), dict.
        Dict and list are returned as String.
        """

        if debug:
            print('val', ast.dump(value))

        # Return constant
        if isinstance(value, ast.Constant):
            return value.value
        # Return just the get_value if possible
        elif isinstance(value, ast.Name) or isinstance(value, ast.Attribute):
            return self.get_value(value)
        # Dict
        elif isinstance(value, ast.Dict):
            return self.parse_dict(value)
        elif isinstance(value, ast.List):
            return self.parse_list(value)

        self.raise_error(None, "Unable to parse the type of the value", ast.unparse(value))

    def get_value(self, value, allowNonStr: bool = False) -> str:
        """
        Gets the value of a string-like value.
        Can be a String or a variable.
        """
        if isinstance(value, ast.Name):
            if value.id.startswith("_"):
                try:
                    return self.labels[value.id[1:]]
                except KeyError:
                    self.raise_error(None, "Label is not found!", value.id)

            return value.id
        elif isinstance(value, ast.Constant):
            if isinstance(value.value, str) or allowNonStr:
                return value.value
            else:
                self.raise_error(None, "Value must be a str!", ast.unparse(value), 2)
        elif isinstance(value, ast.Attribute):
            return self.get_value(value.value) + "." + value.attr
        
    def get_dict(self, dictionary: ast.Dict) -> dict:
        new = {}

        for i in range(len(dictionary.keys)):
            key = dictionary.keys[i]            
            val = dictionary.values[i]

            if isinstance(val, ast.Dict):
                val = self.get_dict(val)
            else:
                val = self.get_value(val)

            if isinstance(key, ast.Name):
                new[key.id] = val
            elif isinstance(key, ast.Constant):
                new[key.value] = val

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
                                temp = {"selector": self.parse_entity((value.value))}

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

    def get_func(self, function: ast.Name | ast.Lambda | ast.Call, filename: str = ""):
        if isinstance(function, ast.Name):
            return f"function {self.namespace}:{function.id.replace('__', '/').lower()}" 
        elif isinstance(function, ast.Lambda):                
            fname = (filename + f'_lmb{self.conditions}').replace('__', '/').lower()
            self.conditions += 1

            code = self.parse([ast.Expr(value=function.body)], fname)
            if code.count('\n') == 0:
                return code
            else:
                self.write(fname, code)
                return f"function {self.namespace}:{fname}"
        elif isinstance(function, ast.Call):
            fname = (filename + f'_lmb{self.conditions}').lower()
            self.conditions += 1

            code = self.parse([ast.Expr(value=function)], fname)
            if code.count("\n") == 0:
                return code
            else:
                self.write(fname, code)
                return f"function {self.namespace}:{fname}"

        self.raise_error(filename, "Not a valid function type", ast.unparse(function), 4)
    
    def warn(self, message: str):
        self.warnings.append(message)

    def get_int(self, value: ast.Constant | ast.UnaryOp, allowNonInt: bool = False):
        """
        Get the integer value of an ast obj.
        If it is negative it uses UnaryOp so this fixes it.
        """
        # If it is negative it is a unary op for some reason
        if isinstance(value, ast.UnaryOp) and isinstance(value.op, ast.USub):
            return -value.operand.value
        elif not (isinstance(value, ast.Constant) and isinstance(value.value, int)) and not allowNonInt:
            self.raise_error(None, "Value must be a valid integer!", ast.unparse(value))
        return value.value

    def command(self, cmd: str, args: list[ast.Constant, ast.Attribute, ast.Name], filename: str = "", expression = None) -> str:
        """
        Extra commands, intended for MC commands
        """
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
                    return f"effect give {self.parse_entity((args[0]))} {self.get_value(args[1])}"
                elif len(args) == 3:
                    return f"effect give {self.parse_entity((args[0]))} {self.get_value(args[1])} {args[2].value}"
                elif len(args) == 4:
                    return f"effect give {self.parse_entity((args[0]))} {self.get_value(args[1])} {args[2].value} {args[3].value}"
                elif len(args) == 5:
                    return f"effect give {self.parse_entity((args[0]))} {self.get_value(args[1])} {args[2].value} {args[3].value} {str(args[4].value).lower()}"
                
            case "cleareffect":
                if len(args) == 1:
                    return f"effect clear {self.parse_entity((args[0]))}"
                elif len(args) == 2:
                    return f"effect clear {self.parse_entity((args[0]))} {self.get_value(args[1])}"

            case "give":
                if len(args) == 2:
                    return f"give {self.parse_entity((args[0]))} {self.get_value(args[1])} 1"
                elif len(args) == 3:
                    return f"give {self.parse_entity((args[0]))} {self.get_value(args[1])} {self.get_lim_num(args[2], min=1)}"
                elif len(args) == 4:
                    components = self.get_dict(args[3])
                    new = []
                    # Due to how MC components work, the first one instead of being : must be =
                    for k, v in components.items():
                        new.append(f"{k}={self.parse_primative_dict(v)}")

                    return f"give {self.parse_entity((args[0]))} {self.get_value(args[1])}[{','.join(new)}] {self.get_lim_num(args[2], min=1)}"
                
            case "summon":
                if len(args) == 1:
                    return f"summon {self.get_value(args[0])}"
                elif len(args) == 2:
                    return f"summon {self.get_value(args[0])} {self.get_value(args[1])}"
                elif len(args) == 3:
                    return f"summon {self.get_value(args[0])} {self.get_value(args[1])} {self.parse_dict(args[2])}"

            case "attribute":
                if len(args) == 2:
                    return f"attribute {self.parse_entity((args[0]))} {self.get_value(args[1])} base get"
                elif len(args) == 3:
                    return f"attribute {self.parse_entity((args[0]))} {self.get_value(args[1])} base set {self.get_lim_num(args[2], -2048, 2048)}"
            case "resetattribute":
                return f"attribute {self.parse_entity((args[0]))} {self.get_value(args[1])} base reset"

            # CREATORS: Just use the RUN function for now.
            # case "bossbar":
            #     match self.get_value(args[0]).lower():
            #         case "add" | "create":
            #             return f"bossbar add {self.}"

            case "dialog":
                if len(args) == 1:
                    return f"dialog clear {self.get_player(args[0])}"
                elif len(args) == 2:
                    return f"dialog show {self.get_player(args[0])} {self.get_value(args[1])}"
                
            case "enchant":
                if len(args) == 2:
                    return f"enchant {self.get_player(args[0])} {self.get_value(args[1])}"
                elif len(args) == 3:
                    return f"enchant {self.get_player(args[0])} {self.get_value(args[1])} {self.get_lim_num(args[2], 1, 5)}"
            
            case "kill":
                return f"kill {self.parse_entity(args[0])}"
            
            case "getplayers":
                player, name = self.parse_var(args[0])
                return f"scoreboard players reset {player} {name}\nexecute at @a run scoreboard players add {player} {name} 1"
            
            case "randint":
                player, name = self.parse_var(args[0])

                return f"execute store result score {player} {name} run random value {self.get_int(args[1])}..{self.get_int(args[2])}"

            case "tellraw":
                return f"tellraw {self.get_player(self.get_value(args[0]))} {json.dumps(self.fstring(args[1]))}"
               
            case "actionbar":
                return f"title {self.get_player(self.get_value(args[0]))} actionbar {json.dumps(self.fstring(args[1]))}"
            
            case "title":
                return f"title {self.get_player(self.get_value(args[0]))} title {json.dumps(self.fstring(args[1]))}"
            case "subtitle":
                return f"title {self.get_player(self.get_value(args[0]))} subtitle {json.dumps(self.fstring(args[1]))}"
            case "times":
                if len(args) == 4:
                    return f"title {self.get_player(self.get_value(args[0]))} times {self.get_lim_num(args[1])} {self.get_lim_num(args[2])} {self.get_lim_num(args[3])}"
                elif len(args) == 2:
                    return f"title {self.get_player(self.get_value(args[0]))} times {args[1].value}"
                
            case "print":
                return f"tellraw @a {json.dumps(self.fstring(args[0]))}"

            case "say":
                return f"say {args[0].value}"

            case "tparound":
                if len(args) == 2:
                    return f"spreadplayers ~ ~ {args[1].value} {args[1].value} false {self.parse_entity((args[0]))}"
                elif len(args) == 3:
                    return f"spreadplayers ~ ~ {args[1].value} {args[2].value} false {self.parse_entity((args[0]))}"

            case "tag":
                return f"tag {self.parse_entity((args[0]))} add {self.get_value(args[1])}"
            case "removetag":
                return f"tag {self.parse_entity((args[0]))} remove {self.get_value(args[1])}"
            case "inversetag":
                return f"execute store success score .temptag .temp run tag @s add {self.get_value(args[0])}\nexecute if score .temptag .temp matches 0 run tag @s remove {self.get_value(args[0])}"

            case "wait" | "schedule":
                t = self.get_value(args[0], allowNonStr=True)
                
                # Add 't' implying ticks
                if t.isdigit():
                    t += 't'

                return f"schedule function {self.namespace}:{self.get_value(args[1]).replace('__', '/').lower()} {t}"

            case "gamemode":
                return f"gamemode {self.get_value(args[1])} {self.get_player(self.get_value(args[0]))}"

            case "add":
                return self.aug_assign(ast.AugAssign(
                    target = args[0],
                    op = ast.Add(),
                    value = args[1]
                ))

            case "subtract" | "sub":
                return self.aug_assign(ast.AugAssign(
                    target = args[0],
                    op = ast.Sub(),
                    value = args[1]
                ))

            case "multiply" | "mult":
                return self.aug_assign(ast.AugAssign(
                    target = args[0],
                    op = ast.Mult(),
                    value = args[1]
                ))

            case "divide" | "div":
                return self.aug_assign(ast.AugAssign(
                    target = args[0],
                    op = ast.Div(),
                    value = args[1]
                ))

            case "set":
                return self.assign(ast.Assign(
                    targets = [args[0]],
                    value = args[1]
                ))

            case "store":
                entity, varName = self.parse_var(args[0])
                return f"execute store result score {entity} {varName} run {self.get_func(args[1], filename)}"

            case "getdata":
                if len(args) == 2:
                    return f"data get entity {self.parse_entity(args[0])} {self.get_value(args[1])}"
                elif len(args) == 3:
                    return f"data get entity {self.parse_entity(args[0])} {self.get_value(args[1])} {self.get_lim_num(args[2])}"
                
            case "setdata":
                return f"data modify entity {self.parse_entity(args[0])} {self.get_value(args[1])} {self.get_abs_value(args[2])}"

            case _:
                # Call custom function. Args must be of NAME value
                result = []
                if len(args) == 1 and isinstance(args[0], ast.Dict):
                    result.append(f'function {self.namespace}:{cmd.lower()} {self.parse_dict(args[0])}')

                else:
                    for arg in args:
                        val = self.parse_var_only(arg)                       
                        if val in self.variables:
                            if isinstance(self.variables[val], str) and self.variables[val] == 'dummy':
                                entity, varName = self.parse_var(arg)
                                result.append(f"execute store result storage kcf:functionargs {varName} int 1 run scoreboard players get {entity} {varName}")
                            else:
                                result.append(f"data modify storage kcf:functionargs {val} set from storage kcf:vars {val}")

                        elif isinstance(arg, ast.Constant):
                            self.raise_error(filename, "Argument cannot be a pre-defined value. It must be a variable, or be set to a single DICT type", [arg.value, cmd], 2)

                        else:
                            entity, varName = self.parse_var(arg)
                            result.append(f"execute store result storage kcf:functionargs {varName} int 1 run scoreboard players get {entity} {varName}")

                    result.append(f'function {self.namespace}:{cmd.lower()} with storage {self.namespace}:functionargs')

                return "\n".join(result)

        self.raise_error(filename, f"Function '{cmd}' failed to be parsed. Check to see if your arguments are correct.", ast.unparse(expression), 1)

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
    
    def parse_entity(self, value: ast.Name | ast.Constant | ast.Attribute) -> str:
        """
        Parses an obj to an entity.
        Use this instead of self.get_entity(self.get_value((...))
        """
        if isinstance(value, ast.Name) or isinstance(value, ast.Attribute):
            # If it is just a var, use the double method (get ent(get val()))
            return self.get_entity(self.get_value(value))
        elif isinstance(value, ast.Subscript):
            # Get entity - it has to be VAR so double method is used
            ent = self.get_entity(self.get_value(value.value))
            # Get sub
            sub = self.get_value(value.slice)

            # If @ then use [] otherwise use [name=]
            return f"{ent}[{sub}]" if ent.startswith('@') else f"@a[name=\"{ent}\",{sub}]"
        elif isinstance(value, ast.Constant):
            if not isinstance(value.value, str):
                self.raise_warning(None, "Constant entity should be a string datatype", ast.unparse(value))                
            return value.value

        else:
            self.raise_error(None, "Invalid data type for entity!", ast.unparse(value))

    def get_entity(self, entity: str):
        """
        Given a STRING, detect whether it is self, all, etc.
        Newer versions should use the parse_entity instead.
        """
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
                        self.raise_error('?', "Label is not found!", entity)
                return entity
              
    def bool_to_if(self, value: bool):
        if value:
            y = "if"
            n = "unless"
        else:
            y = 'unless'
            n = 'if'

        return y, n
    
    def parse_condition(self, condition, starting = 'execute ', opp = False):
        """
        Complex algorithm that parses a conditional statement obj.
        Currently does not work with OR statement.
        """
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
                        temp += f"{y} entity {self.parse_entity(value.args[0])} "
                    case "block":
                        temp += f"{y} block {self.get_value(value.args[0])} {self.get_value(value.args[1])} "
                    case "tag":
                        if len(value.args) == 1:
                            temp += f"{y} entity @s[tag={self.get_value(value.args[0])}] "
                        elif len(value.args) == 2:
                            temp += f"{y} entity {self.parse_entity((value.args[0]))}[tag={self.get_value(value.args[1])}] "
                        else:
                            self.raise_error(None, "Tag condition has an invalid number of arguments!", ast.unparse(value))
                    case "custom":
                        temp += value.args[0].value + " "

            elif isinstance(value, ast.UnaryOp) and isinstance(value.op, ast.Not):
                return cmpre(value.operand, not opp)
            elif isinstance(value, ast.BoolOp):
                if isinstance(value.op, ast.And):
                    for v in value.values:
                        cmpre(v, opp)
                elif isinstance(value.op, ast.Or):
                    temp += 'run '
                    t = []
                    for v in value.values:
                        t.append(self.parse_condition(v, opp=opp))
                    temp += f'\n{temp}'.join(t)
                    add = False
            elif isinstance(value, ast.Constant):
                if isinstance(value.value, str):
                    temp += f"{y} {value.value} "
                elif value.value == False:
                    # Put a random FALSE statement
                    temp += "unless score 1 p-numbers = 1 p-numbers"
            
        cmpre(condition, opp)

        if add:
            return temp + "%end%"
        else:
            return temp.replace("execute run ", '')
        
    def parse_var(self, expression: ast.Attribute | ast.Name) -> tuple[str, str]:
        """
        Gets the entity and variable name of an ast obj
        """
        if isinstance(expression, ast.Constant) and isinstance(expression.value, str):
            if "." in expression.value:
                entity, varName = expression.value.split('.', 1)
                a, b = self.get_entity(entity), varName
            else:
                a, b = "#global", expression.value
        elif isinstance(expression, ast.Attribute):
            if isinstance(expression.value, ast.Attribute):
                d, e = self.parse_var(expression.value)
                a, b = d, e + "." + expression.attr
            else:
                a, b = self.parse_entity(expression.value), expression.attr
        elif isinstance(expression, ast.Name):
            a, b = "#global", expression.id
        else:
            self.raise_error(None, "Variable cannot be parsed - it is not a valid type.", ast.unparse(expression), 4)
        
        if b not in self.variables:
            self.variables[b] = 'dummy'

        return a, b

    def parse_var_only(self, expression: ast.Attribute | ast.Name) -> str:
        """
        Only get the name of the variable, not the entity.
        """
        if isinstance(expression, ast.Attribute):
            if isinstance(expression.value, ast.Attribute):
                a, b = self.parse_var(expression.value)
                return a + '.' + b + "." + expression.attr

            return self.get_value(expression.value) + '.' + expression.attr
        elif isinstance(expression, ast.Name):
            return expression.id
        
    def write(self, filename: str, data: str):
        """
        Write the file to the memory.
        Use the write_files to write the saved data into disk.
        """

        filename = filename.replace('__', "/").lower()
        if filename not in self.files:
            self.files[filename] = data
        else:
            if self.files[filename] == '':
                self.files[filename] = data
            else:
                self.files[filename] += "\n" + data

    def print(self):
        for file in self.files:
            print(f"\nIN FILE {file}.mcfunction:\n" + self.files[file])

    def inverse_parse_var(self, var: str):
        """
        Inversely parses a var, or turns a String into an ast.Name or ast.Attribute.
        Intended for reverse usage, such as the add/sub/.. functions.
        """

        if '.' in var:
            splitted = var.split('.', )

            a = splitted[-1]
            v = '.'.join(splitted[:-1])

            if '.' in v:
                v = self.inverse_parse_var(v)
            else:
                v = ast.Name(id=v)

            return ast.Attribute(value=v, attr=a)
        else:
            return ast.Name(id=var)

    def aug_assign(self, expression: ast.AugAssign):
        if isinstance(expression.value, ast.Constant) and isinstance(expression.value.value, str):
            expression.value = self.inverse_parse_var(expression.value.value)

        if isinstance(expression.value, ast.Constant) or isinstance(expression.value, ast.UnaryOp):
            # Must be var, so
            var = expression.target
            # If self, e.g.
            entity, varName = self.parse_var(var)

            value = self.get_int(expression.value, allowNonInt=True)

            # MC does not accept -1 adds/removes
            opp = False
            if value < 0 and type(expression.op) in (ast.Add, ast.Sub):
                opp = True
                value *= -1

            if isinstance(expression.op, ast.Add):
                return (f"scoreboard players {'remove' if opp else 'add'} {entity} {varName} {value}")
            elif isinstance(expression.op, ast.Sub):
                return (f"scoreboard players {'add' if opp else 'remove'} {entity} {varName} {value}")
            else:

                if isinstance(expression.op, ast.Mult) or isinstance(expression.op, ast.Div) or isinstance(expression.op, ast.FloorDiv):
                    # For decimals, use 2 commands to essnetially give a best rounded answer.
                    if isinstance(value, float):
                        value = self.get_int(expression.value, allowNonInt=True)

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
                target=expression.target,
                op=expression.op,
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
            entity1, varName1 = self.parse_var(expression.value)
            
            var = expression.target

            entity, varName = self.parse_var(var)

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
        if isinstance(expression.value, ast.Dict):
            for var in expression.targets:
                temp.append(f"data modify storage kcf:vars {self.parse_var_only(var)} set value {self.parse_dict(expression.value)}")

        elif isinstance(expression.value, ast.List):
            for var in expression.targets:
                temp.append(f"data modify storage kcf:vars {self.parse_var_only(var)} set value {self.parse_list(expression.value)}")

        elif isinstance(expression.value, ast.Constant) or isinstance(expression.value, ast.UnaryOp):
            # Must be var, so
            for var in expression.targets:
                # If self, e.g.                    
                # # IF LABEL, aka starts with _:
                if isinstance(var, ast.Name) and var.id.startswith("_"):
                    self.labels[var.id[1:]] = self.get_int(expression.value, allowNonInt=True)

                else:
                    # If integer:
                    value = self.get_int(expression.value, allowNonInt=True)
                    
                    if isinstance(value, int):
                        entity, varName = self.parse_var(var)

                        if varName not in self.variables:
                            self.variables[varName] = "dummy"

                        temp.append(f"scoreboard players set {entity} {varName} {value}")

                    else:
                        if type(value) in (str, float, bool, list):
                            var = self.parse_var_only(var)
                            self.variables[var] = value

                            # Parsed value
                            if isinstance(value, str):
                                parsedValue = f'"{value}"'
                            elif isinstance(value, bool):
                                parsedValue = '1b' if value else '0b'
                            else:
                                parsedValue = value

                            temp.append(f"data modify storage kcf:vars {var} set value {parsedValue}")
                        else:
                            self.raise_error(None, f"Variable '{var}' is not a valid type! It is neither a scoreboard (int) or a storage (str, dict, float, bool)", ast.unparse(value), 2)
                        
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
                if varName1 not in self.variables:
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

        fname = fname.replace('__', '/')

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
        
    def parse_dict(self, data: ast.Dict):
        values = []

        for i in range(len(data.keys)):
            k = data.keys[i]
            v = data.values[i]

            if isinstance(v, ast.Dict):
                values.append(f"{k.value}: {self.parse_dict(v)}")
            else:
                values.append(f"{k.value}: {v.value}")

        return '{' + ", ".join(values) + '}'
    
    def parse_primative_dict(self, data: dict):
        
        # {'abc': 1, 'def': {'abc': 1}}
        values = []

        for k, v in data.items():
            if isinstance(v, dict):
                v = self.parse_dict(v)
            values.append(f"{k}: {v}")

        return '{' + ", ".join(values) + '}'

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
                        funcname = funcname.replace('__', '/')
                        cmds.append(f"function {self.namespace}:{funcname}")
                    else:
                        args = expression.value.args
                        func = expression.value.func.id

                        match func:
                            case "run":
                                # If F string
                                if isinstance(args[0], ast.JoinedStr):
                                    temp = ""
                                    for v in args[0].values:
                                        if isinstance(v, ast.Constant):
                                            temp += v.value
                                        elif isinstance(v, ast.FormattedValue):
                                            temp += f"$({v.value.id})"

                                    if not temp.startswith('$'):
                                        temp = '$' + temp

                                    cmds.append(temp)
    
                                else:
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
                                cmd = self.command(func, args, filename, expression)
                                cmds.append(cmd)
                # IF
                elif isinstance(expression.value, ast.IfExp):
                    cmds.append(self.ifexpr(expression.value, filename))
                else:
                    if not (isinstance(expression.value, ast.Constant) and isinstance(expression.value.value, str)):
                        self.raise_warning(filename, f"Expression '{ast.unparse(expression)}' is skipped.", ast.unparse(expression))
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

                self.write(fname, self.parse(expression.body, fname) +"\n" + temp)
                 
                # Add 1 to the condition counter
                self.conditions += 1
            elif isinstance(expression, ast.For):
                fname = f"{filename}_for{self.conditions}"

                # Get the variable name
                var = expression.target.id

                # Add to global vars
                if var not in self.variables:
                    self.variables[var] = "dummy"

                # Get the range
                if isinstance(expression.iter, ast.Call) and expression.iter.func.id == "range":
                    args = expression.iter.args

                    def get(arg: ast.Constant | ast.Name | ast.Attribute):
                        if isinstance(arg, ast.Constant):
                            value = arg.value
                            if value not in self.pNumbers:
                                self.pNumbers.append(value)
                            
                            return f"{value} p-numbers"
                        else:
                            return ' '.join(self.parse_var(arg))
                        
                    # Create a constant so the get function would work
                    # Get function auto inits pNumbers
                    step = get(ast.Constant(value=1))
                    start = get(ast.Constant(value=0))

                    if len(args) == 1:
                        end = get(args[0])
                    elif len(args) == 2:
                        start = get(args[0])
                        end = get(args[1])
                    elif len(args) == 3:
                        start = get(args[0])
                        end = get(args[1])
                        step = get(args[2])

                    cmds.append(f"scoreboard players operation #global {var} = {start}\nfunction {self.namespace}:{fname}")

                    self.write(fname, self.parse(expression.body, fname) +f"\nscoreboard players operation #global {var} += {step}\nexecute if score #global {var} < {end} run function {self.namespace}:{fname}")
                    
                    self.conditions += 1

            elif isinstance(expression, ast.Return):
                # if isinstance(expression.value)
                try:
                    if isinstance(expression.value, ast.Constant) or isinstance(expression.value, ast.UnaryOp):
                        cmds.append(f"return {self.get_int(expression.value)}")
                    else:
                        cmds.append(f"return run {self.get_func(expression.value)}")

                except AttributeError:
                    cmds.append(f"return fail")
            else:
                if not (isinstance(expression, ast.ImportFrom) and expression.module == 'KCFSyntax') and not isinstance(expression, ast.Pass):
                    self.raise_warning(filename, f"Expression '{ast.unparse(expression)}' is skipped.", ast.unparse(expression))
                if isinstance(expression, ast.Pass):
                    cmds.append('\0')
        try:
            return "\n".join(cmds)
        except TypeError:
            # Search through
            i = cmds.index(None)
            kw = ast.unparse(parsed[i])

            self.raise_error(filename, "[parse] Cannot parse expression.", kw, 2)


    def raise_error(self, filename: str, message: str, keywords: str = None, error_level: int = 3):
        """
        Raises an error to the user.
        Filename and keywords could be NONE.

        Error level specifies the level of error occurred.
        1. Not extreme but may cause some issues and should be avoided
        2. May break code and should be avoided
        3. Will break code
        4. Will break code definitely
        5. Extreme disallowed.

        Therefore if the ERROR_THRESHOLD is set to 5+, all custom errors are ignored
        """

    
        
        ErrorMessage = self.raise_message(filename, message, keywords)  

        if error_level < self.ERROR_THRESHOLD:
            self.warn(ErrorMessage)
        else:
            raise TypeError(ErrorMessage)
    
    def raise_warning(self, filename: str, message: str, keywords: str = None):
        """
        Adds a warning to the user but will not stop the code
        """

        ErrorMessage = self.raise_message(filename, message, keywords)

        if self.ERROR_THRESHOLD <= 0:
            raise TypeError(ErrorMessage)
        else:
            self.warn(ErrorMessage)

    def raise_message(self, filename: str, message: str, keywords: str = None):
        try:
            if keywords is not None:
                # Keyword may be list, in that case
                if type(keywords) == str:
                    keywords = [keywords]


                # Find line
                lines = self.code.splitlines()

                lastFunc = ".;'\\."
                b = False
                for i in range(len(lines)):
                    for kw in keywords:
                        kw = str(kw)
                        if (kw in lines[i]) and (filename is None or filename == '?' or filename.lower().startswith(lastFunc.lower())):
                            ln = i + 1
                            line = lines[i].strip()
                            b = True                
                        
                    if lines[i].startswith("def "):
                        lastFunc = lines[i][4:].split('(')[0]
                    if b:
                        break
                else:
                    ln = '?'
                    line = '?'

                # If ?
                if filename == '?' or filename is None:
                    filename = lastFunc

                # Create nice ^^^
                ind = line.index(str(keywords[0]))
                locText = (' ' * ind) + ('^' * len(str(keywords[0])))

                msg = f"{message}\n  Detected to occur at line {ln} position {ind+1}, in function '{filename}':\n    {line}\n    {locText}"
            else:
                msg = message
        except Exception as e:
            msg = message

        return msg

    def add_extras(self):
        # REMOVE \0
        for file in self.files:
            lines = []
            for line in self.files[file].splitlines():
                if '\0' not in line:
                    lines.append(line)
            self.files[file] = '\n'.join(lines)

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
        codeTree = ast.parse(self.code).body
        self.parse(codeTree)
        self.add_extras()

    def print_warnings(self):
        if len(self.warnings) > 0:
            print("== WARNINGS ==")
            for i in range(len(self.warnings)):
                warning = self.warnings[i]

                print(f"{i+1}. {warning}")

    def print_stats(self):
        """Prints stats like how much lines are saved and etc."""
        print("== STATISTICS ==")
        totalChar = 0
        lns = 0
        for file in self.files:
            totalChar += len(self.files[file].replace("\n\n","\n"))
            lns += self.files[file].replace("\n\n","\n").count('\n')

        nowchar = len(self.code.replace("\n\n","\n"))
        nowlns = self.code.replace("\n\n","\n").count('\n')

        print(f"Characters Saved: {totalChar - nowchar} ({nowchar} chars in code compared to {totalChar} chars in MCF)")
        print(f"Lines Saved: {lns - nowlns} ({nowlns} lines in code compared to {lns} lines in MCF)")

    def write_files(self, destination: str = "."):
        for file, contents in self.files.items():
            files = file.split('/')
            if not os.path.isdir(os.path.join(destination, *files[:-1])):
                os.mkdir(os.path.join(destination, *files[:-1]))
            with open(os.path.join(destination, *files[:-1], files[-1] + ".mcfunction"), 'w', encoding='utf-8') as f:
                f.write(contents)
