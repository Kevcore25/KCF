"""
Simple flask application
"""
PACK_VERSION = 71
import traceback
from flask import Flask, request, jsonify, send_file, make_response
import io
import subprocess, json
import sys
import tempfile
import zipfile
import os, ast
import KCFPy
import shutil

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/compile', methods=['POST'])
def compile():
    try:
        data = request.get_json()
        code = data.get('code', '')
        filename = data.get('filename', 'datapack.zip')

        name = 'tempdp'
        
        if not code:
            return jsonify({'error': 'No code provided'}), 400
        
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.zip', delete=False) as f:
            output_path = f.name
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.zip', delete=False) as f:
            std_output_path = f.name

        try:
            original_stdout = sys.stdout
            with open(std_output_path, 'w') as f:
                sys.stdout = f
                try:

                    # Get Code
                    print("Getting code...")
                    codeTree = ast.parse(code)

                    print("Initializing KCF...")
                    t = KCFPy.KCF(codeTree.body)

                    # Modify namespace
                    t.namespace = "kcf"

                    print("Building code...")
                    # Build to memory
                    t.build()

                    # Print to console - optional
                    # t.print()

                    print("Creating datapack structure...")
                    # Create datpack
                    join = os.path.join

                    def mkfile(file: str, value: str = ""):
                        with open(file, "w") as f:
                            f.write(value)

                    def mkdir(path: str):
                        if not os.path.isdir(path):
                            os.mkdir(path)

                    namespace = 'kcf'

                    mkdir(name)
                    mkdir(join(name, "data"))
                    mkfile(join(name, "pack.mcmeta"), json.dumps({
                        "pack": {
                            "pack_format": PACK_VERSION,
                            "description": "Created with KCF-Py Version 1.0"
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

                    destination = "."

                    mkdir(destination)

                    dest = join(destination, name, "data", namespace, "function")

                    t.write_files(dest)

                    print("Zipping file")
                    # with zipfile.ZipFile(output_path, 'w') as zipf:
                    #     for file_path in os.listdir(os.path.join(destination, name)):
                    #         zipf.write(file_path)
                    shutil.make_archive('tempfile', 'zip', os.path.join(destination, name))

                    print("Done! Printed contents:")

                    t.print()
                finally:
                    sys.stdout = original_stdout
            
            # Read the generated output
            with open('tempfile.zip', 'rb') as f:
                output_content = f.read()

            with open(std_output_path, 'r') as f:
                std = f.read()
            
            # Create a response with the file data
            response = make_response(output_content)
            response.headers['Content-Disposition'] = f'attachment; filename={filename}'
            response.headers['Content-Type'] = 'text/plain'
            response.headers['Code-Output'] = std.replace("\n","%nl;%")
            
            return response
                
        except Exception as e:
            return str(e), 400
        finally:
            if os.path.exists(output_path):
                os.unlink(output_path)

            try:
                shutil.rmtree(name)
                os.remove('tempfile.zip')
            except: pass
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)