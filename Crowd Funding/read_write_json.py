import json
import os

current_folder = os.path.dirname(os.path.abspath(__file__))
Users_Data = os.path.join(current_folder, "users.json")
Projects_Data = os.path.join(current_folder, "projects.json")

def load_json(filename):
    try:
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f"Error happened {filename}: {e}")
        return []

def save_json(filename, data):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error happened {filename}: {e}")