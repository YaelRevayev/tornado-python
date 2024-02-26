import unittest
import csvtojson
import constant
import os


class TestCalculations(unittest.TestCase):
    global data
    data = {
        "33718276": {"name": "Yael", "age": 20},
        "11143445": {"name": "Noa", "age": 21},
    }
    global dir_name
    dir_name = "Yael"

    def test_creating_new_dir(self):
        csvtojson.create_dir(dir_name)
        self.assertIn(
            dir_name,
            os.listdir("."),
            msg="Dir has not been created in current path",
        )

    def test_creation_of_json_file(self):
        csvtojson.write_dict_to_json(data, 0, dir_name)
        file_name = "{0}{1}".format(constant.JSON_FILE_PREFIX, 0)
        self.assertIn(
            file_name,
            os.listdir("./{0}".format(dir_name)),
            msg="File has not been created in current directory",
        )


if __name__ == "__main__":
    unittest.main()
