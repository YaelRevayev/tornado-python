import unittest
import sys
import os
sys.path.append(os.getcwd())
import extract_from_csv


class TestExtract(unittest.TestCase):
    global data
    data = [
        {"MDACODE": "Yael", "age": "20", "hobby": "read"},
        {"MDACODE": "Noa", "age": "21", "hobby": "dance"},
    ]

    def test_extracting_valid(self):
        records = extract_from_csv.extract_records_from_csv_to_list("./tests/test_data.csv")
        self.assertEqual(
            records,
            data,
            msg="Extraction is not valid",
        )

    def test_extracting_src_path_invalid(self):
        with self.assertRaises(Exception):
            extract_from_csv.extract_records_from_csv_to_list(".nonExistingPath")


if __name__ == "__main__":
    unittest.main()
