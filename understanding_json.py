import json
import os

# Define the file path
file_path = os.path.join("data", "bike_points_test.json")

# Load the JSON file
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
    print("JSON file loaded successfully!")
    print(f"Data type: {type(data)}")
    print(f"Keys: {list(data.keys()) if isinstance(data, dict) else 'Not a dictionary'}")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except json.JSONDecodeError:
    print("Invalid JSON format")
except Exception as e:
    print(f"Error loading file: {e}")

print(data)