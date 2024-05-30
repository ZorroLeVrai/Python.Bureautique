import sys
import os

# Add the directory containing code.py to sys.path
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Lib'))
sys.path.insert(0, lib_path)

# Import code module
import code

# Example usage of a function from code.py
code.print_hello()