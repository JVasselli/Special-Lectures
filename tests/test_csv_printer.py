import unittest
from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read1(self):
        printer = CSVPrinter("tests/sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))
    
    def test_read2(self):
        printer = CSVPrinter("tests/sample.csv")
        l = printer.read()
        for i, row in enumerate([1, 2, 3]):
            for j, column in enumerate(['A', 'B', 'C']):
                self.assertEqual(l[i][j], f"value{row}{column}")

    def test_throw_exception(self):
        printer = CSVPrinter("non_existant_file.csv")
        with self.assertRaises(FileNotFoundError):
            _ = printer.read()
