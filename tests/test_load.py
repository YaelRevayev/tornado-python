import unittest
import os
import shutil
import sys
sys.path.append(sys.path.append(r"C:\Users\rabay\OneDrive\שולחן העבודה\hafifot-tornado\tornado_python")
)
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

    def test_write_to_json_one_file(self):
        os_operations.create_dir("test-people")

        load.write_json(two_records_data, "./{}".format("test-people"))
        self.assertEqual(len(os.listdir("test-people")), 1)

        shutil.rmtree("test-people")

    def test_write_to_json_more_than_one_file(self):
        os_operations.create_dir("test-people")
        
        load.write_json(four_records_Data, "./{}".format("test-people"))
        self.assertEqual(len(os.listdir("test-people")), 2)

        shutil.rmtree("test-people")

    def test_grouping_records_to_list_valid(self):
        list = load.grouping_records_from_list(two_records_data)
        expected_list = [{'Yael': {'MDACODE': 'Yael', 'age': '20', 'hobby': 'read'},
                           'Noa': {'MDACODE': 'Noa', 'age': '21', 'hobby': 'yoga'}}]  
        self.assertEqual(list, expected_list)

    def test_grouping_records_to_list_empty_list(self):
        list = load.grouping_records_from_list([])
        self.assertEqual(list, [])


if __name__ == "__main__":
    unittest.main()
