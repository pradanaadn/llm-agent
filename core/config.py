import os
import sys


def setup_python_path():
    # Clear the sys.path and add only the current working directory and its parent
    sys.path.clear()

    # Add the current working directory
    current_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(current_dir)

    # Add the parent directory to the Python path
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    sys.path.append(parent_dir)

    # Print the Python path for debugging
    print("Python path:", sys.path)


setup_python_path()
