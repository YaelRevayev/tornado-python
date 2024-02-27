import unittest
import os
import shutil
import load
import extract
import os_operations


class TestFileConverting(unittest.TestCase):
    global data
    data = [
        {"MDACODE": "Yael", "age": "20", "hobby": "read"},
        {"MDACODE": "Noa", "age": "21", "hobby": "dance"},
    ]

    def test_extracting_valid(self):
        records = extract.extract_records_from_csv_to_list("./src/test_data.csv")
        self.assertEqual(
            records,
            data,
            msg="Extraction is not valid",
        )

    def test_creating_new_dir_empty_dir_name(self):
        with self.assertWarns(UserWarning):
            os_operations.create_dir("")

    def test_extracting_src_path_invalid(self):
        with self.assertRaises(Exception):
            extract.extract_records_from_csv_to_list(".nonExistingPath")

    def test_write_to_json_less_than_one_group(self):
        os_operations.create_dir("test-people")
        data = [
            {
                "Yael": {"MDACODE": "Yael", "age": 20, "hobby": "read"},
                "Noa": {"MDACODE": "Noa", "age": 21, "hobby": "dance"},
            }
        ]
        load.write_dict_to_json_file(data, "./{}".format("test-people"))
        print(len(os.listdir("test-people")))
        self.assertEqual(len(os.listdir("test-people")), 1)
        # shutil.rmtree("test-people")


if __name__ == "__main__":
    unittest.main()
