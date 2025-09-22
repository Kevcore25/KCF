"""

"Compiles" the code based on the build configuration file.
It is not really compiling, but rather "translating" the file instead.
In KCF, I will call it "building" but know that it is more of a "translating" process.

"""

CONFIG_FILE = r"BuildConfig.json"

PACK_VERSION = 80 # 71 is 1.21.5

import json, KCFPy
import shutil, os

# Welcome message
print('\n' + '=' * os.get_terminal_size()[0] + "\n")
print(f"KC Function Builder Version {KCFPy.VERSION}")
print("Create Minecraft Datapacks with Python!")
print(f"\n{KCFPy.VERSION} Highlights: {KCFPy.VERSION_HIGHLIGHTS}")
print('=' * os.get_terminal_size()[0] + "\n")

# Get config
print("Obtaining Configuration...")
with open(CONFIG_FILE, 'r') as f:
    configs = json.load(f)

namespace = configs['MCFunction Namespace']
name = configs['Datapack Name']
source = configs['Build Source File']
finaldestination = configs['Build Destination']
description = configs['Datapack Description']
error_threshold = configs['Error Threshold']
zipison = configs['Zip file']

# Get Code
print("Getting code...")
with open(source, 'r', encoding='utf-8') as f:
    code = f.read()

print("Initializing KCF...")
t = KCFPy.KCF(code)

# Modify vars
t.namespace = namespace
t.ERROR_THRESHOLD = error_threshold

print("Building code...")
# Build to memory
t.build()

# Create datpack
print("Creating datapack structure...")

join = os.path.join

def mkfile(file: str, value: str = ""):
    with open(file, "w") as f:
        f.write(value)

def mkdir(path: str):
    if not os.path.isdir(path):
        os.mkdir(path)

if zipison:
    # Create a temp folder for now
    # Later, it will ZIP the file to conserve disk + make it easier for SAMBA
    destination = 'kcftempbuildfolder'
    if os.path.isdir(destination):
        shutil.rmtree(destination, ignore_errors=True)
    os.mkdir(destination)
    os.chdir(destination)
else:
    destination = finaldestination
    mkdir(destination)
    os.chdir(destination)

    # Delete
    print("Deleting old files...")

    if os.path.isdir(name):
        shutil.rmtree(name, ignore_errors=True)

# Write
print("Writing code...")

t.write_files(name)

if zipison:
    # Zip fi1le
    print("Zipping files...")
    zipname = os.path.join(finaldestination, name)
    shutil.make_archive(zipname, 'zip', root_dir=name, verbose=True)

    # print("Copying ZIP file to location...")
    # shutil.copyfile(zipname, finaldestination)

    print("Cleaning up...")
    # os.remove(zipname)
    os.chdir('..')
    shutil.rmtree("kcftempbuildfolder")

# print("Done!")
# input("Press enter to continue...\t")
t.print()
t.print_stats()
t.print_warnings()