"""
## KCF Documentation Library
Library with no features.
It serves only for syntax highlighting for KCF.

If you are programming with KCF, this is almost a must-have.
It specifies valid functions to use and its arguments.
"""

from items import *
from blocks import *
from entities import *
from effects import *

entity = lambda Entity: "Entity condition for conditional statements"
block = lambda Position, Block: "Block condition for conditional statements"

class SelectorEntity: str
self: SelectorEntity
all: SelectorEntity
randomplayer: SelectorEntity
nearest: SelectorEntity
nearestplayer: SelectorEntity
every: SelectorEntity

class SetblockHandler: "The handler for setblock"
replace: SetblockHandler
destroy: SetblockHandler
keep: SetblockHandler
class FillHandler(SetblockHandler): "The handler for fill"
hollow: FillHandler
outline: FillHandler

class function: "A defined function"
class Label: "A generic label to replace some types.\n\nLabels are global once declared, so ideally it should be at the top of the file.\n\nHowever, you may want to add them when needed for organization."

class Player: "A player name, label, or selector"

def run(Command: str):
    """
    Runs a Minecraft command.
    It is the most basic command that will be used with every complex code.
    
    Example: `run("give @a diamond_sword")`
    """

def label(Label: str, Value: str):
    """
    Labels something to be used in entities or block.
    Ideally, labels should be used at the top of files, since they are global once declared.
    However, for organization purposes, it may be wise to put it in a function instead.

    Example: `label("spawn", "0 0 0")`

    You can also label by setting a variable with a underscore.
    Underscore variables are labels and therefore cannot be used as variables.
    
    Example: `_spawn = "0 0 0"`
    """

def execute(*, Values: str, Function: function):
    """
    Executes a function.

    Example: `execute("as @a at @s", my_function)`

    Example 2: `execute("postitioned ~ ~ ~", "as @a", my_function)`
    """


def var(Name: str, Type: str = "int"):
    """
    Declares a variable with a type. Type is optional.

    Example: `var("deaths", "deathCount")`

    Example 2: `var("i")`
    """

def trigger(Name: str):
    """
    Declares a trigger variable that will automatically be enabled for all players.

    Example:
    ```
    def load():
        # Triggers should always be in the load function
        trigger("hello")

    # triggers__<name>() is called when a player runs the trigger
    def triggers__hello():
        run("say World!")
    ```
    """

def setblock(Position: str | Label, Block: Block | str, Handler: SetblockHandler):
    """
    Runs a setblock command.

    Example: `setblock("0 0 0", bedrock)`

    ```
    Example 2: 
    ```
    # Labels must start with underscore (_)
    _spawn = "0 0 0"
    setblock(_spawn, "bedrock", replace)
    ```
    """

def fill(StartPosition: str | Label, EndPosition: str | Label, Block: Block | str, Handler: FillHandler | SetblockHandler):
    """
    Runs a fill command.

    Example: `fill("-10 0 -10", "10 0 10", bedrock)`

    Example 2:
    ``` 
    # Labels must start with underscore (_)
    _pos1 = "-10 0 -10"
    _pos2 = "10 0 10" 
    fill(_pos1, _pos2, "bedrock", hollow)
    ```
    """

def give(Player: SelectorEntity | str | Label, Item: Item | str, Count: int = 1, ItemComponents: dict = None):
    """
    Gives an item to a player.
    If ItemComponents is specified, the item MUST be of Item type and not a string for compatability.
    Otherwise, it may break the code.

    Example: `give(all, "diamond_sword")`

    Example 2:
    ```
    # Labels must start with underscore (_)
    _within10 = "@a[distance=..10]"
    give(_within10, diamond_sword, 1, {enchantments: {unbreaking: 3}})
    ```
    """

def effect(Entity: SelectorEntity | str | Label, Effect: Effect | str, Duration: int = 30, Amplifier: int = 0):
    """
    Gives an effect to an entity.
    Use the cleareffect function to clear an effect for an entity.

    Example: `effect(all, slowness)`

    Example 2:
    ```
    # Labels must start with underscore (_)
    _within10 = "@a[distance=..10]"
    effect(_within10, slowness, 10, 1)
    ```
    """

def cleareffect(Entity: SelectorEntity | str | Label, Effect: Effect | str):
    """
    Clears an effect from an entity.

    Example: `cleareffect(all, slowness)`
    """

def attribute(Entity: SelectorEntity | str | Label, Attribute: str, Value: int):
    """
    Set a base value for an attribute for an entity.

    Example: `attribute(self, max_health, 20)`
    """

def summon(Entity: Entity | str | Label, Position: str = "~ ~ ~", Properties: dict = {}):
    """
    Summon an entity. You should not need to use a label, although it is allowed.

    Example: `summon(zombie)`

    Example 2: `summon(zombie, "~ ~ ~", {glowing: true})`
    """