import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
print("Current working directory:", os.getcwd())
print("Python path:", sys.path)
print("Contents of the current directory:", os.listdir(os.getcwd()))

try:
    import workout_api.main
    print("Module imported successfully")
except Exception as e:
    print(f"Error importing module: {e}")
