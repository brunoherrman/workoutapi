import os
import sys

# Adiciona o diretório do script ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
print("Current working directory:", os.getcwd())
print("Python path:", sys.path)
print("Contents of the current directory:", os.listdir(os.getcwd()))

try:
    import workout_api
    print("Module 'workout_api' imported successfully")
    try:
        import workout_api.main
        print("Module 'workout_api.main' imported successfully")
    except Exception as e:
        print(f"Error importing 'workout_api.main': {e}")
except Exception as e:
    print(f"Error importing 'workout_api': {e}")
