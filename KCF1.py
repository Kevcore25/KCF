import json

from equationparser import convert_equation

namespace = "kcf"

def is_simple(expr):
    expr = expr.strip()
    while expr.startswith('(') and expr.endswith(')'):
        expr = expr[1:-1].strip()
    if '(' in expr or ')' in expr:
        return False
    for op in ['+', '-', '*', '/']:
        if op in expr:
            return False
    return True

def get_compound_op(op):
    if op == '+':
        return '+='
    elif op == '-':
        return '-='
    elif op == '*':
        return '*='
    elif op == '/':
        return '/='
    else:
        return None

def break_down(expr, provided_target, type_str, temp_count, is_top_level, overall_target):
    expr = expr.strip()
    stack = []
    for i in range(len(expr)):
        if expr[i] == '(':
            stack.append(i)
        elif expr[i] == ')':
            if stack:
                stack.pop()
    if not stack and len(expr) > 0 and expr[0] == '(' and expr[-1] == ')':
        return break_down(expr[1:-1], provided_target, type_str, temp_count, is_top_level, overall_target)
    
    min_precedence = 3
    pos = -1
    stack = []
    for i, c in enumerate(expr):
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                stack.pop()
        elif not stack:
            if c in ['+', '-', '*', '/']:
                precedence = 1 if c in ['+', '-'] else 2
                if precedence <= min_precedence:
                    min_precedence = precedence
                    pos = i
                    
    if pos == -1:
        step = provided_target + " = " + expr + ";"
        return ([step], provided_target, temp_count)
    
    op_char = expr[pos]
    left_expr = expr[:pos].strip()
    right_expr = expr[pos+1:].strip()
    
    if is_top_level:
        steps_left, left_var, temp_count = break_down(left_expr, provided_target, type_str, temp_count, False, overall_target)
        if is_simple(right_expr):
            right_var = right_expr
            steps_right = []
        else:
            right_temp = str(temp_count) + ".temp"
            temp_count += 1
            steps_right, right_var, temp_count = break_down(right_expr, right_temp, None, temp_count, False, overall_target)
        steps = steps_left + steps_right
        op_assign = get_compound_op(op_char)
        step_op = provided_target + " " + op_assign + " " + right_var + ";"
        steps.append(step_op)
        return (steps, provided_target, temp_count)
    else:
        steps_left, left_var, temp_count = break_down(left_expr, provided_target, None, temp_count, False, overall_target)
        if is_simple(right_expr):
            right_var = right_expr
            steps_right = []
        else:
            right_temp = str(temp_count) + ".temp"
            temp_count += 1
            steps_right, right_var, temp_count = break_down(right_expr, right_temp, None, temp_count, False, overall_target)
        op_assign = get_compound_op(op_char)
        step_op = provided_target + " " + op_assign + " " + right_var + ";"
        steps = steps_left + steps_right + [step_op]
        return (steps, provided_target, temp_count)

def convert_equation(line):
    line = line.strip()
    if not line.endswith(';'):
        return ["Error: Input must end with a semicolon."]
    line = line.rstrip(';').strip()
    if '=' not in line:
        return ["Error: Input must contain an assignment."]
    
    parts = line.split('=', 1)
    lhs_part = parts[0].strip()
    rhs = parts[1].strip()
    
    if ' ' in lhs_part:
        words = lhs_part.split()
        type_str = ' '.join(words[:-1])
        lhs = words[-1]
    else:
        type_str = None
        lhs = lhs_part
        
    steps, final_var, _ = break_down(rhs, lhs, type_str, 0, True, lhs)
    
    if type_str is not None:
        for i, step in enumerate(steps):
            stripped_step = step.lstrip()
            if stripped_step.startswith(lhs + " = "):
                new_step = type_str + " " + stripped_step
                if step != stripped_step:
                    spaces = step[:len(step) - len(stripped_step)]
                    new_step = spaces + new_step
                steps[i] = new_step
                break
    return steps

class Function:
    def __init__(self, code: str):
        self.code = code

class Parser:
    lambdanum = 0

    def __init__(self, code: str):     
        self.code = code   
        self.removeComments()

        self.code = self.code.replace("\n", ";")

        self.code = self.code.replace("++", " += 1")
        self.code = self.code.replace("--", " -= 1")



    def removeComments(self):
        newcode = []
        for line in self.code.splitlines():
            if not line.lstrip().startswith("//"):
                newcode.append(line.strip())
        
        self.code = "\n".join(newcode)

    def getEnclosedParenthesis(self, i):
        unclosed = 0 if self.code[i] == "{" else 1

        for j in range(i, len(self.code)):
            t = self.code[j]

            if t == '{':
                unclosed += 1
            elif t == "}":
                unclosed -= 1

            if unclosed <= 0:
                return self.code[i+1:j]
        return self.code[i+1:j]

    def getEnclosedBrackets(self, i):

        unclosed = 0 if self.code[i] == "(" else 1

        for j in range(i, len(self.code)):
            t = self.code[j]

            if t == '(':
                unclosed += 1
            elif t == ")":
                unclosed -= 1

            if unclosed <= 0:
                return self.code[i+1:j]
 
    def getEnclosedBracketLoc(self, i):
        unclosed = 0
        found = False
        for j in range(i, len(self.code)):
            t = self.code[j]
            if t == '{':
                found = True
                unclosed += 1
            elif t == "}":
                unclosed -= 1

            if unclosed <= 0 and found:
                return j
                     
    def getKeywordBefore(self, i: int):
        return self.code[:i].split(" ")[-1]  

    def onIfStatement(self, i, statement):
        # Get ( loc
        loc = self.code[i:].index("(") + i
        condition = self.getEnclosedBrackets(loc)

        # Get code
        loc = self.code[loc:].index("{") + loc 
        code = self.getEnclosedParenthesis(loc)  

        # Return parsed code
        return [statement, condition, Parser(code).parse()]

    def getUntilChar(self, i):
        temp = []
        for t in self.code[i:]:
            if t.lower() not in "-+*/ ;":
                temp.append(t)
            else:
                break
        return "".join(temp)
    
    def getUntilCharB(self, i):
        temp = []
        for t in self.code[:i][::-1]:
            if t.lower() not in "-+*/ ;":
                temp.append(t)
            else:
                break
        return "".join(temp[::-1])
    
    def getUntilSemi(self, i, char=';'):
        return self.code[i+1:self.code[i:].index(char) + i]

    def getNextSemiIndex(self, i, char=';'):
        return self.code[i:].index(char) + i

    def get_function(self, i, parsed):
        """
        Could be: function();
        or: []() {
        
        }
        """

        func = self.code[i:self.code[i:].index('()') + i].strip()

        if func == '[]':
            loc = self.getEnclosedBracketLoc(i)

            self.lambdanum += 1

            parsed.append(["func", f"lambda{self.lambdanum}", Parser(self.getEnclosedParenthesis(self.code[i:].index('{') + i)).parse()])

            return f"lambda{self.lambdanum}", loc

        else:
            return func, self.getNextSemiIndex(i)


    def sep_var(self, var):
        """
        Example 1: int var = a + b;
        =
        int var = a;
        var = b;

        Example 2: var = a * b + 1
        =
        var = a;
        var *= b;
        var += 1

        Example 3: var = ((1 - 3) + (a * b) - 2)

        int b0 = a
        b0 *= b

        int b1 = 1
        b1 -= 3

        """

        return convert_equation(var)
    def parse(self):
        parsed = []

        temp = ""

        i = 0
        while (i < len(self.code)):
            t = self.code[i]

            if t == " ":
                print(temp)
                match temp:
                    case "if" | "unless":
                        parsed.append(self.onIfStatement(i, temp))

                        i = self.getEnclosedBracketLoc(i) + 1

                        temp = ""

                    case "execute":
                        end = self.code[i+1:].index('>') + i
                        tempparsed = self.code[i+1:end].split(" ")
                        tempparsed.insert(0, "execute")

                        func, loc = self.get_function(end + 2, parsed)

                        tempparsed.append(['runfunc', func])

                        parsed.append(tempparsed)

                        i = loc
                    
                    case "int" | "let":
                        varname = self.getUntilChar(i+1)
                        if "=" in self.code[i:self.code[i:].index(";") + i]:
                            value = self.code[i:].split('=')[1].strip()
                            parsed.append(['var', 'dummy', varname, value[:(value.index(';'))]])
                        else:
                            parsed.append(['var', 'dummy', varname])

                        i = self.getNextSemiIndex(i)

                    case "-=" | "+=" | "*=" | "/=" | "%=":
                        # GET VAR NAME
                        varname = self.getUntilCharB(i-3)

                        # GET VALUE
                        value = self.getUntilChar(i+1)
                        parsed.append([temp, varname, value])

                        i = self.getNextSemiIndex(i)

                    case "=": 
                        # DECLARE TO VAR
                        # abc = asedf
                        var1 = self.getUntilCharB(i-2)
                        var2 = self.getUntilSemi(i)

                        parsed.append(["set", var1, var2])

                        i = self.getNextSemiIndex(i)

                    case "#label" | "tell":
                        # Get line
                        line = self.code[i+1:self.code[i:].index(";") + i]

                        name, values = line.split(" ", 1)

                        parsed.append([temp.replace("#", ""), name, values])

                        i = self.getNextSemiIndex(i)

            
                    case _:
                        if temp.endswith("()"):
                            print("CODE", self.code[i:])
                            funcCode = self.getEnclosedParenthesis(self.code[i:].index("{") + i)
                            print("code,", funcCode)

                            parsed.append(["func", temp[:-2], Parser(funcCode).parse()])

                            i = self.getEnclosedBracketLoc(i+1) + 1
                        elif temp.startswith("/") and not temp.startswith("//"):
                            parsed.append(["cmd", temp[1:] + self.code[i:self.code[i:].index(";")+i]])
                            i = self.code[i:].index(";")+i
                        temp = ""
    
            elif t == ";":    
                # RUN Function
                temp = temp.lstrip(';')

                print("temp", temp)

                if temp.endswith("()"):
                    parsed.append(["runfunc", temp[:-2]])
                # CMD
                temp = ""


            else: 
                temp += t   

            i += 1
        return parsed


class Translate:
    """
    Converts parsed KCF into a list of MCFunction files
    """
    labels = {}

    ifs = 0

    precision = 2

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
                if entity.startswith("#"):
                    try:
                        return self.labels[entity[1:]]
                    except KeyError:
                        raise Exception("Label is not found!")
                return entity

    def parse_get_var(self, var: str):
        if "." in var:
            entity, varname = var.split('.', 2)
            return [self.get_entity(entity), varname]
        elif var.isdigit():
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


    def parse_condition(self, condition: str):

        if condition is None:
            raise Exception("There is no condition: " + str(self.currentP))

        splitted = condition.split(' ')


        # CASES:
        # something == something
        # if (@e[distance=..5])

        if len(splitted) == 3: # prob var == something 
            # Detect COORDS, in case: (#yes == block)
            if (splitted[0].startswith("#")):
                return self.parse_condition(condition.replace(splitted[0], self.labels[splitted[0][1:]]))

            var1 = self.parse_get_var(splitted[0])
            op = splitted[1]

            if splitted[2].isdigit() and op != "!=":
                match op:
                    case ">": 
                        var2 = str(int(splitted[2]) + 1) + ".."
                    case "<": 
                        var2 = ".." + str(int(splitted[2]) - 1)
                    case ">=": 
                        var2 = splitted[2] + ".."
                    case "<=": 
                        var2 = ".." + splitted[2]
                    case _:
                        var2 = splitted[2]

                return f"score {var1[0]} {var1[1]} matches {var2}"

            else:
                var2 = self.parse_get_var(splitted[2])

                if op == "==":
                    op = "="

                return f"score {var1[0]} {var1[1]} {op} {var2[0]} {var2[1]}"
        elif len(splitted) == 5:
            # Coords

            return f"block {var1[0]} {var1[1]}{var2[2]} {var2[4]}"
        else:
            return f"entity {self.get_entity(condition)}"

    def translate(self, parsed: list, filename = ""):
        cmds = []

        for p in parsed:
            self.currentP = p
            match p[0]:
                case "label":
                    self.labels[p[1]] = p[2]

                case "if" | "unless":
                    newfilename = filename + "_if" + str(self.ifs)

                    print("IN FILE " + newfilename + ".mcfunction:\n" + self.translate(p[2], newfilename))

                    cmds.append("execute " + p[0] + " " + self.parse_condition(p[1]) + f" run function {namespace}:{newfilename}")

                    self.ifs += 1

                case "set":
                    var1 = self.parse_get_var(p[1])

                    # If 2 is int
                    if p[2].isdigit():
                        cmds.append(f"scoreboard players set {var1[0]} {var1[1]} {p[2]}")

                    else:
                        var2 = self.parse_get_var(p[2])
                        cmds.append(f"scoreboard players operation {var1[0]} {var1[1]} = {var2[0]} {var2[1]}")

                case "func":
                    print(f"IN FILE {p[1]}.mcfunction:\n" + self.translate(p[2], p[1]))
                case "var":
                    cmds.append(f"scoreboard objectives add {p[2]} {p[1]}")
                    if len(p) == 4:
                        cmds.append(f"scoreboard players set #global {p[2]} {p[3]}")

                case "runfunc":
                    cmds.append(f"function {namespace}:{p[1]}")

                case "-=" | "+=":
                    entity, var = self.parse_get_var(p[1])

                    if p[2].isdigit():
                        if p[0] == "-=":
                            cmds.append(f"scoreboard players remove {entity} {var} {p[2]}")
                        else:
                            cmds.append(f"scoreboard players add {entity} {var} {p[2]}")
                    else:
                        entity2, var2 = self.parse_get_var(p[1])
                        cmds.append(f"scoreboard players operation {entity} {var} {p[0]} {entity2} {var2}")

                case "*=" | "/=":
                    entity, var = self.parse_get_var(p[1])

                    if p[2].isdigit():
                        if p[0] == "-=":
                            cmds.append(f"scoreboard players remove {entity} {var} {p[2]}")
                        else:
                            cmds.append(f"scoreboard players add {entity} {var} {p[2]}")
                    elif " " in p[2]:
                        pass
                    elif p[2].replace(".", "").isdigit():
                        value = round(float(p[2]) * 10 ** self.precision)
                        if p[0] == "*=":
                            cmds.append(f"scoreboard players operation {entity} {var} *= {value}")
                            cmds.append(f"scoreboard players operation {entity} {var} /= {10 ** self.precision}")
                        else:
                            cmds.append(f"scoreboard players operation {entity} {var} /= {value}")
                            cmds.append(f"scoreboard players operation {entity} {var} *= {10 ** self.precision}")

                    else:
                        entity2, var2 = self.parse_get_var(p[1])
                        cmds.append(f"scoreboard players operation {entity} {var} {p[0]} {entity2} {var2}")

                case "tell":
                    cmds.append(f"tellraw {self.get_player(p[1])} {self.parse_message(p[2])}")


                case "execute":
                    func = p[-1][1]

                    i = 1
                    temp = ["execute"]
                    while True:
                        cmd = p[i]

                        if cmd == p[-1]:
                            break

                        match cmd:
                            case "as" | "at":
                                temp.append(cmd)
                                temp.append(self.get_entity(p[i+1]))
                            case "positioned" | "pos":
                                temp.append("positioned")
                                if p[i+1].startswith('#'):
                                    pos = self.labels[p[i+1][1:]]

                                    temp.append(pos)
                                else:
                                    temp.append(p[i+1], p[i+2], p[i+3])
                                    i += 3
                            case "if" | "unless":
                                temp.append(cmd)
                                temp.append(self.parse_condition([p[i+1]]))

                        i += 1

                    temp.append(f"run function {namespace}:{func}")

                    cmds.append(" ".join(temp))
                case "cmd":
                    cmds.append(p[1])
            
        return "\n".join(cmds)
    

class Validity:
    """
    Determines if a parsed KCF will contain errors. It will give warnings when building, but it will not stop the compling process unless there is an error.

    Example:

    load() {
        private let var1 = 100;

        // Variable "useless" is declared and of int type, yet it is never used in any function
        int useless;

        // No errors
        trigger uselessTrigger;
    }
    
    function1() {
        // Error: "var1" is private and only allowed within function "function"
        var1 = 30;

        function();
    }

    function() {
        // Variable "var1" is supposedly constant, yet it is changed        
        var1 = 30; 

        // Variable "var3" is never declared
        var3 = 30; 

        // Unknown command "killall"
        /killall player;

        // Variable "var5" is never declared
        if (var5 == 1) {
            function1();
        }

   

        // Variable "i" is possibly declared multiple times. Follow good practices by declaring your variables in the load() function
        // // SIDENOTE: This is because "function1" runs function()
        int i = 0;
        
        // Label "spawn" is never used
        #label spawn 0 0 0;
    }

    """

p = Parser(
"""
setblock() {
    /setblock $(coordX) $(coordY) $(coordZ) air
}

function() {
    int i = 0;

    while (true) {
        i++;

        store coords.coordX = i + 1;
        store coords.coordY = i - 5;
        store coords.coordZ = i * 3;

        setblock(coords);

        if (i > 50) {
            break;
        }
    }

}



"""
    ).parse()

print(json.dumps(p, indent=4))

"""

"""
print(Translate().translate(p))


"""



"""