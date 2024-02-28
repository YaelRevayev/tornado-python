import unittest
import sys
import os
sys.path.append(r"C:\Users\rabay\OneDrive\שולחן העבודה\hafifot-tornado\tornado_python")
import extract


class TestExtract(unittest.TestCase):
    global data
    data = [
        {"MDACODE": "Yael", "age": "20", "hobby": "read"},
        {"MDACODE": "Noa", "age": "21", "hobby": "dance"},
    ]

    def test_extract_csv_gets_valid_path_returns_records_to_list(self):
        records = extract.extract_csv("./tests/test_data.csv")
        self.assertEqual(
            records,
            data,
            msg="Extraction is not valid",
        )

    def test_extract_csv_gets_invalid_path_returns_exception(self):
        with self.assertRaises(Exception):
            extract.extract_csv(".nonExistingPath")


if __name__ == "__main__":
    unittest.main()
