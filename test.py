import unittest
import csvtojson
import constant
import os


class TestCalculations(unittest.TestCase):

    def test_creation_of_json_file(self):
        serial_for_test = 1
        print(csvtojson.create_serial_json_file(constant.DIR_NAME, serial_for_test))
        file_name = "{0}{1}".format(constant.JSON_FILE_PREFIX, serial_for_test)
        self.assertIn(
            file_name,
            os.listdir("./{0}".format(constant.DIR_NAME)),
            msg="File has not been created in current directory",
        )


if __name__ == "__main__":
    unittest.main()
