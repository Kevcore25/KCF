"""

"Compiles" the code based on the build configuration file

"""

CONFIG_FILE = r"BuildConfig.json"

PACK_VERSION = 71 # 71 is 1.21.5

import json, ast, KCF2

# Get config
print("Obtaining Configuration...")
with open(CONFIG_FILE, 'r') as f:
    configs = json.load(f)

namespace = configs['MCFunction Namespace']
name = configs['Datapack Name']
source = configs['Build Source File']
destination = configs['Build Destination']
description = configs['Datapack Description']

# Get Code
print("Getting code...")
with open(source, 'r') as f:
    codeTree = ast.parse(f.read())

print("Initializing KCF...")
t = KCF2.KCF(codeTree.body)

# Modify namespace
t.namespace = namespace

print("Building code...")
# Build to memory
t.build()

# Print to console - optional
# t.print()

print("Creating datapack structure...")
# Create datpack
import os

join = os.path.join

def mkfile(file: str, value: str = ""):
    with open(file, "w") as f:
        f.write(value)

def mkdir(path: str):
    if not os.path.isdir(path):
        os.mkdir(path)

mkdir(name)
mkdir(join(name, "data"))
mkfile(join(name, "pack.mcmeta"), json.dumps({
    "pack": {
        "pack_format": PACK_VERSION,
        "description": description
    }
}, indent=4))

mkdir(join(name, "data", namespace))
mkdir(join(name, "data", namespace, "function"))

mkdir(join(name, "data", "minecraft"))
mkdir(join(name, "data", "minecraft", "tags"))
mkdir(join(name, "data", "minecraft", "tags", "function"))

mkfile(join(name, "data", "minecraft", "tags", "function", "load.json"), json.dumps({
    "values": [
        f"{namespace}:load"
    ]
}))
mkfile(join(name, "data", "minecraft", "tags", "function", "tick.json"), json.dumps({
    "values": [
        f"{namespace}:tick"
    ]
}))

# Write
print("Writing code...")

mkdir(destination)

dest = join(destination, name, "data", namespace, "function")

t.write_files(dest)

print("Done!")
input("Press enter to continue...\t")