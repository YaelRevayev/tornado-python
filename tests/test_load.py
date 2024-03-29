import unittest
import os
import shutil
import sys
import json

sys.path.append(sys.path.append(os.getcwd()))
import load
import os_operations

class TestLoad(unittest.TestCase):
    global two_records_data
    two_records_data = [
        {"MDACODE": "Yael", "age": "20", "hobby": "read"},
        {"MDACODE": "Noa", "age": "21", "hobby": "yoga"},
    ]

    global four_records_Data
    four_records_Data = [
                {"MDACODE": "Yael", "age": 20, "hobby": "read"},
                {"MDACODE": "Noa", "age": 21, "hobby": "yoga"},
                {"MDACODE": "Shani", "age": 21, "hobby": "piano"},
                {"MDACODE": "Eitan", "age": 20, "hobby": "football"},
        ]
    
    def count_keys_in_json_file(self, json_file_path):
        with open(json_file_path, 'r') as f:
            data = json.load(f)
        return len(data.keys())

    def test_load_json_gets_two_records_writes_to_one_file(self):
        os_operations.create_dir("test-people")
        load.load(two_records_data, "./{}".format("test-people"),2)
        self.assertEqual(self.count_keys_in_json_file("test-people/mada1"), 2)
        shutil.rmtree("test-people")

    def test_load_json_gets_four_records_writes_to_two_files(self):
        os_operations.create_dir("test-people")
        
        load.load(four_records_Data, "./{}".format("test-people"),2)
        self.assertEqual(self.count_keys_in_json_file("test-people/mada1"), 4)

        shutil.rmtree("test-people")

    def test_grouping_records_to_list_gets_two_records_returns_list_of_dicts(self):
        list = load.grouping_records_from_list(two_records_data)
        expected_list = [{'Yael': {'MDACODE': 'Yael', 'age': '20', 'hobby': 'read'},
                           'Noa': {'MDACODE': 'Noa', 'age': '21', 'hobby': 'yoga'}}]  
        self.assertEqual(list, expected_list)

    def test_grouping_records_to_list_gets_no_records_returns_empty_list(self):
        list = load.grouping_records_from_list([])
        self.assertEqual(list, [])


   
    

if __name__ == "__main__":
    unittest.main()
