import unittest
import sys
import os
sys.path.append(os.getcwd())
import os_operations


class TestOsOperations(unittest.TestCase):
    global data
    data = [
        {"MDACODE": "Yael", "age": "20", "hobby": "read"},
        {"MDACODE": "Noa", "age": "21", "hobby": "dance"},
    ]

    def test_creating_new_dir_empty_dir_name(self):
        with self.assertWarns(UserWarning):
            os_operations.create_dir("")


if __name__ == "__main__":
    unittest.main()
