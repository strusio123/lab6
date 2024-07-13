
import json
def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Plik {file_path} nie istnieje.")
        return None
    except json.JSONDecodeError:
        print(f"Błąd dekodowania pliku {file_path}.")
        return None
if __name__ == "__main__":
    file_path = "path/to/your/json/file.json"
    json_data = read_json_file(file_path)
    if json_data:
        print(json_data)
