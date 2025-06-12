"""
Library with no features.
It serves only for syntax highlighting for KCF

"""

from items import *
from blocks import *
from entities import *

class SelectorEntity: str
self: SelectorEntity
all: SelectorEntity
randomplayer: SelectorEntity
nearest: SelectorEntity
nearestplayer: SelectorEntity
every: SelectorEntity

class SetblockHandler: str
replace: SetblockHandler
destroy: SetblockHandler
hollow: SetblockHandler
outline: SetblockHandler

class function: str
class Label: str

def run(Command: str):
    """
    Runs a Minecraft command
    
    Example: run("give @a diamond_sword")
    """

def label(Label: str, Value: str):
    """
    Labels something to be used in entities or block.
    Ideally, labels should be used at the top of files.

    Example: label("spawn", "0 0 0")

    You can also label by setting a variable with a underscore.
    Example: _spawn = "0 0 0"
    """

def execute(*, Values: str, Function: function):
    """
    Executes a function.

    Example: execute("as @a at @s", my_function)
    Example 2: execute("postitioned ~ ~ ~", "as @a", my_function)
    """


def var(Name: str, Type: str):
    """
    Declares a variable with a type. Type is optional.
    """

def trigger(Name: str):
    """
    Declares a trigger variable that will automatically be enabled for all players
    """

# def setblock(Position: str | Label, Block: Block | str, Handler: SetblockHandler):
#     """
#     Runs a setblock command
#     """