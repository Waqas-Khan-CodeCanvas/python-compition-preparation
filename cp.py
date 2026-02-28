import marshal
import dis

with open("./__pycache__/test.cpython-313.pyc", "rb") as f:
    f.read(16)  # skip header
    code = marshal.load(f)

dis.dis(code)