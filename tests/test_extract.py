import unittest
import extract
from ...tornado_python import extract


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

    def test_extracting_src_path_invalid(self):
        with self.assertRaises(Exception):
            extract.extract_records_from_csv_to_list(".nonExistingPath")


if __name__ == "__main__":
    unittest.main()
