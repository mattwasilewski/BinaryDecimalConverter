import unittest
from converter import Converter;
from unittest.mock import patch
import io

class TestConverter(unittest.TestCase):
    
    def setUp(self):
        self.converter = Converter()


    def test_validate_binary_input(self):
        self.assertEqual(self.converter.validate_binary_input("1010"), "1010")
        self.assertIsNone(self.converter.validate_binary_input("1021"))
        self.assertIsNone(self.converter.validate_binary_input(""))

    def test_validate_decimal_input(self):
        self.assertEqual(self.converter.validate_decimal_input("123"), "123")
        self.assertIsNone(self.converter.validate_decimal_input("12a3"))
        self.assertIsNone(self.converter.validate_decimal_input(""))

    def test_binary_to_decimal(self):
        self.assertEqual(self.converter.binary_to_decimal("1010"), 10)
        self.assertEqual(self.converter.binary_to_decimal("0"), 0)
        self.assertIsNone(self.converter.binary_to_decimal("102"))
        self.assertIsNone(self.converter.binary_to_decimal(""))

    def test_decimal_to_binary(self):
        self.assertEqual(self.converter.decimal_to_binary("10"), "1010")
        self.assertEqual(self.converter.decimal_to_binary("0"), "0")
        self.assertIsNone(self.converter.decimal_to_binary("10a"))
        self.assertIsNone(self.converter.decimal_to_binary(""))


    @patch('builtins.input', side_effect=['1', '1010', 'exit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_binary_to_decimal(self, mock_stdout, mock_input):
        self.converter.convert()
        self.assertIn('1010 w systemie dziesiętnym to: 10', mock_stdout.getvalue())


    @patch('builtins.input', side_effect=['2', '10', 'exit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_decimal_to_binary(self, mock_stdout, mock_input):
        self.converter.convert()
        self.assertIn('10 w systemie binarnym to: 1010', mock_stdout.getvalue())


    @patch('builtins.input', side_effect=['3', 'exit'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_convert_invalid_choice(self, mock_stdout, mock_input):
        self.converter.convert()
        self.assertIn('Błędny wybór. Wybierz 1, 2 lub wpisz \'exit\'.', mock_stdout.getvalue())



if __name__ == "__main__":
    unittest.main()