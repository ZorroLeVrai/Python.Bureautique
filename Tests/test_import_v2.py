import importlib.util as ilu
import sys
import os

# Define the module name and file path
module_name = 'code'
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Lib/code.py'))

# Load the module
spec = ilu.spec_from_file_location(module_name, module_path)
code = ilu.module_from_spec(spec)
sys.modules[module_name] = code
spec.loader.exec_module(code)

# Example usage of a function from code.py
code.print_hello()
