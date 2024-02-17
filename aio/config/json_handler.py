import json


class JsonHandler:
    def __init__(self, file_path=None, data=None):
        self.file_path = file_path
        self.data = data if data is not None else {}

    def load_from_file(self, file_path=None):
        file_path = file_path or self.file_path
        try:
            with open(file_path, 'r') as file:
                self.data = json.load(file)
            return True
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except json.JSONDecodeError as e:
            print(f"Decode error {file_path}: {e}")
        except Exception as e:
            print(f"Read file error{file_path}: {e}")
        return False

    def get_value(self, key, default=None):
        return self.data.get(key, default)
