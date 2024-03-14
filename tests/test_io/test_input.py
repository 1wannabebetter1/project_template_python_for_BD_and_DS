import unittest
from app.io.input import read_from_file, read_pandas

TEST_FOLDER = "test_folder/"


class TestReadFromFile(unittest.TestCase):
    def test_empty_file(self):
        file_path = TEST_FOLDER + "empty.txt"
        expected_content = ""
        content = read_from_file(file_path)
        self.assertEqual(content, expected_content)

    def test_file_not_found(self):
        file_path = "non_existent.txt"
        content = read_from_file(file_path)
        self.assertEqual(content, "File not found")

    def test_file_with_content(self):
        file_path = TEST_FOLDER + "sample.txt"
        expected_content = "asfoakg['paosdjkg'lkasdjmfl;'kasjf;l'aksdjnf"
        content = read_from_file(file_path)
        self.assertIn(expected_content, content)


class TestReadPandas(unittest.TestCase):
    def test_csv_size(self):
        file_path = TEST_FOLDER + "sample.csv"
        data = read_pandas(file_path)
        self.assertIsNotNone(data)
        self.assertTrue(data.shape == (1000, 4))

    def test_csv_file_not_found(self):
        file_path = TEST_FOLDER + "non_existent.csv"
        data = read_pandas(file_path)
        self.assertEqual(data, None)

    def test_csv_file_with_content(self):
        file_path = TEST_FOLDER + "sample.csv"
        expected_columns = ['id', 'firstname', 'lastname', 'email']
        data = read_pandas(file_path)
        self.assertIsNotNone(data)
        self.assertListEqual(list(data.columns), expected_columns)


if __name__ == "__main__":
    unittest.main()
