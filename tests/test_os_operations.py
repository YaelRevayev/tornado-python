import unittest
import sys
import os
#os.getcwd()
sys.path.append(r"C:\Users\rabay\OneDrive\שולחן העבודה\hafifot-tornado\tornado_python")
import os_operations


class TestOsOperations(unittest.TestCase):
    def test_creating_new_dir_valid(self):
        os_operations.create_dir("test123")
        self.assertTrue(os.path.isdir('test123'))


if __name__ == "__main__":
    unittest.main()
