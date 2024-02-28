import unittest
import os
import shutil
import sys
sys.path.append(os.getcwd())
import load
import os_operations

class TestLoad(unittest.TestCase):
    global data
    data = [
        {"MDACODE": "Yael", "age": "20", "hobby": "read"},
        {"MDACODE": "Noa", "age": "21", "hobby": "yoga"},
    ]

    def test_write_to_json_one_file(self):
        os_operations.create_dir("test-people")
        data = [
            {
                "Yael": {"MDACODE": "Yael", "age": 20, "hobby": "read"},
                "Noa": {"MDACODE": "Noa", "age": 21, "hobby": "yoga"},
            }
        ]
        load.write_dict_to_json_file(data, "./{}".format("test-people"))
        print(len(os.listdir("test-people")))
        self.assertEqual(len(os.listdir("test-people")), 1)
        shutil.rmtree("test-people")

    def test_write_to_json_more_than_one_file(self):
        os_operations.create_dir("test-people")
        data = [
            {
                "Yael": {"MDACODE": "Yael", "age": 20, "hobby": "read"},
                "Noa": {"MDACODE": "Noa", "age": 21, "hobby": "yoga"},
            },
            {
                "Shani": {"MDACODE": "Shani", "age": 21, "hobby": "piano"},
                "Eitan": {"MDACODE": "Eitan", "age": 20, "hobby": "football"},
            },
        ]
        load.write_dict_to_json_file(data, "./{}".format("test-people"))
        print(len(os.listdir("test-people")))
        self.assertEqual(len(os.listdir("test-people")), 2)
        shutil.rmtree("test-people")

    def test_grouping_records_to_list_valid(self):
        list = load.grouping_records_from_list(data, 1)
        expected_list = [
            {"Yael": {"MDACODE": "Yael", "age": "20", "hobby": "read"}},
            {"Noa": {"MDACODE": "Noa", "age": "21", "hobby": "yoga"}},
        ]
        self.assertEqual(list, expected_list)

    def test_grouping_records_to_list_empty_list(self):
        list = load.grouping_records_from_list([], 1)
        self.assertEqual(list, [])


if __name__ == "__main__":
    unittest.main()
