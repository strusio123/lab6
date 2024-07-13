
import json

def write_json_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print(f"Dane zapisano do pliku {file_path}.")
    except IOError:
        print(f"Błąd zapisu do pliku {file_path}.")

if __name__ == "__main__":
    data_to_save = {"key": "value"}
 
    file_path = "path/to/your/output.json"
    write_json_file(data_to_save, file_path)
