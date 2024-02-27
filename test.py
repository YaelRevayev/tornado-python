import unittest
import csvtojson
import constant
import os
import warnings


class TestFileConverting(unittest.TestCase):
    global data
    data = {
        "33718276": {"name": "Yael", "age": 20},
        "11143445": {"name": "Noa", "age": 21},
    }
    global dir_name
    dir_name = "Yael"

    def test_creating_new_dir_valid_name(self):
        csvtojson.create_dir(dir_name)
        self.assertIn(
            dir_name,
            os.listdir("."),
            msg="Dir has not been created in current path",
        )

    def test_creating_new_dir_empty_name(self):
        with self.assertWarns(UserWarning):
            csvtojson.create_dir("")

    def test_creation_of_json_file_valid_args(self):
        csvtojson.write_dict_to_json(data, 0, dir_name)
        file_name = "{0}{1}".format(constant.JSON_FILE_PREFIX, 0)
        self.assertTrue(
            os.path.exists("./{0}/{1}".format(dir_name, file_name)),
            msg="File has not been created in current directory",
        )

    def test_creation_of_json_file_invalid_dir_name(self):
        pass

    def test_creation_of_json_file_empty_dir(self):
        pass

    def test_creation_of_josn_file_negative_group_num(self):
        pass

    def test_csv_to_json_less_than_one_group(self):
        pass

    def test_csv_to_json_only_one_group(self):
        pass

    def test_csv_to_json_more_than_one_group(self):
        pass


if __name__ == "__main__":
    unittest.main()
