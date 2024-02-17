import unittest
from main import Schema
import json

class TestSchema(unittest.TestCase):

    def setUp(self):
        # Create a temporary test schema file
        test_data = {"message": {"key1": "value1", "key2": 42, "key3": ["option1", "option2"]}}
        with open('test_data.json', 'w') as f:
            json.dump(test_data, f)

    def tearDown(self):
        # Clean up the temporary test schema file
        import os
        os.remove('test_data.json')

    def test_valid_schema_creation(self):
        # Test if the schema is created successfully with valid data
        schema = Schema('test_data.json')
        self.assertTrue(isinstance(schema, Schema))

    def test_invalid_schema_creation(self):
        # Test if KeyError is raised when the schema is created with invalid data
        with self.assertRaises(FileNotFoundError):
            Schema('invalid_data.json')

    def test_invalid_message_key(self):
        # Test if KeyError is raised when the schema is created with invalid data
        with self.assertRaises(KeyError):
            Schema('test_data_without_message.json')

    def test_run_loop(self):
        # Test the run_loop method with a simple schema
        schema = Schema('test_data.json')
        expected_result = {'user': 
                                {'type': 'ARRAY', 'tag': '', 'description': '', 'required': False}, 
                            'time': 
                                {'type': 'INTEGER', 'tag': '', 'description': '', 'required': False}, 
                            'acl': 
                                {'type': 'ENUM', 'tag': '', 'description': '', 'required': False}, 
                            'publicFeed': 
                                {'type': 'BOOL', 'tag': '', 'description': '', 'required': False}, 
                            'internationalCountries': 
                                {'type': 'ENUM', 'tag': '', 'description': '', 'required': False}, 
                            'topTraderFeed': 
                                {'type': 'BOOL', 'tag': '', 'description': '', 'required': False}}
        self.assertEqual(schema.run_loop(), expected_result)

    def test_extended_run_loop(self):
        # Test the run_loop method with extended set to True
        schema = Schema('test_data.json', extended=True)
        expected_result = {'user': 
                           {'type': 'ARRAY', 
                                'tag': '', 
                                'properties': 
                                    {'id': 
                                        {'type': 'STRING', 
                                         'tag': '', 
                                         'description': '', 
                                         'required': False}, 
                                    'nickname': 
                                        {'type': 'STRING', 
                                         'tag': '', 
                                         'description': '', 
                                         'required': False}, 
                                    'title': 
                                        {'type': 'STRING', 
                                         'tag': '', 
                                         'description': '', 
                                         'required': False}, 
                                    'accountType': 
                                        {'type': 'STRING', 
                                        'tag': '', 'description': 
                                         '', 'required': False}, 
                                    'countryCode': 
                                        {'type': 'STRING', 
                                         'tag': '', 
                                         'description': '', 
                                         'required': False}, 
                                    'orientation': 
                                        {'type': 'STRING', 
                                        'tag': '', 
                                        'description': '', 
                                        'required': False}}, 
                                    'description': '', 
                                    'required': False}, 
                                    'time': 
                                        {'type': 'INTEGER', 
                                         'tag': '', 
                                         'description': '', 
                                         'required': False}, 
                                    'acl': 
                                        {'type': 'ENUM', 
                                         'tag': '', 
                                         'description': '', 
                                         'required': False}, 
                                    'publicFeed': 
                                        {'type': 'BOOL', 
                                        'tag': '', 
                                        'description': '', 
                                        'required': False}, 
                                    'internationalCountries': 
                                        {'type': 'ENUM', 
                                         'tag': '', 
                                         'description': '', 
                                         'required': False}, 
                                    'topTraderFeed': 
                                        {'type': 'BOOL', 
                                         'tag': '', 
                                         'description': '', 
                                         'required': False}}
        self.assertEqual(schema.run_loop(), expected_result)

if __name__ == '__main__':
    unittest.main()
