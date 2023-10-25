from flask import Flask
import subprocess

app = Flask(__name__)


@app.post("/<int:vm_id>/start")
def start_vm(vm_id):
    try:
        completed = subprocess.run(["qm", "start", f"{vm_id}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=True)
        return f"{completed.stdout}"
    except Exception as err:
        return f"{err.}"
