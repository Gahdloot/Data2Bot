from typing import Dict, List, Union
import json

class Schema:

    def __init__(self, location: str, extended: bool = False) -> None:
        try:

            with open(location) as file:
                data = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Cannot find this file")
        
        except Exception as exc:
            raise exc("Unhandled Error Found")

        self.message = data.get("message")
        if self.message is None:
            raise KeyError("Invalid schema format")
        self.extended = extended

    def run_loop(self, recurring: Union[bool, dict] = False) -> Dict:
        result = {}
        message = self.message if not recurring else recurring

        for key, value in message.items():
            if isinstance(value, str):
                result[key] = self.handle_string()
            elif isinstance(value, bool):
                result[key] = self.handle_bool()
            elif isinstance(value, int):
                result[key] = self.handle_int()
            elif isinstance(value, list):
                result[key] = self.handle_enum()
            elif isinstance(value, dict):
                result[key] = self.handle_dict(value)
            else:
                result[key] = self.handle_unhandled(type(value))

        return result
    
    def process_data(self, filename: str ='schema_3.json') -> bool:
        data = self.run_loop()
        with open(f'schema/{filename}', 'w') as file:
            json.dump(data, file, indent=4)
        return True

    def handle_string(self) -> Dict:
        return Schema.schema_value("STRING")
        

    def handle_int(self) -> Dict:
        return Schema.schema_value("INTEGER")
            

    def handle_enum(self) -> Dict:
        return Schema.schema_value("ENUM")
    
    def handle_bool(self) -> bool:
        return Schema.schema_value("BOOL")


    def handle_unhandled(self, tp: type) -> Dict:
        return Schema.schema_value(str(tp).upper())

    def handle_dict(self, message: dict) -> Dict:
        properties = self.run_loop(message)
        if not self.extended:
            return Schema.schema_value("ARRAY")
        return {
            "type": "ARRAY",
            "tag": "",
            "properties": properties,
            "description": "",
            "required": False
        }
    @staticmethod
    def schema_value(typ: str) -> Dict:
        return {
            "type": typ.upper(),
            "tag": "",
            "description": "",
            "required": False
        }

