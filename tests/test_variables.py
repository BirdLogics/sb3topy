"""
Unit tests for variables

TODO Finish creating tests for Value
TODO Create tests Variable
"""

import math
import sys
import unittest

sys.path.insert(0, '../')
try:
    from engine.variables import Value, Variable
except ImportError:
    from src.engine.variables import Value, Variable


class ValueTests(unittest.TestCase):
    """Contains tests for the Value class"""

    def test_float(self):
        """Tests the __float__ method"""

        # float() will throw an error if type is not float

        result = float(Value(3))
        self.assertEqual(result, 3, "Value modified")

        result = float(Value('5'))
        self.assertEqual(result, 5, "String not casted")

        result = float(Value(' 7 '))
        self.assertEqual(result, 7, "Whitespace sensitive cast")

        # Special values
        result = float(Value('test'))
        self.assertEqual(result, 0, "String cast != 0")

        result = float(Value(float('nan')))
        self.assertEqual(result, 0, "Float nan cast != 0")

        result = float(Value('nan'))
        self.assertEqual(result, 0, "String 'nan' cast != 0")

        result = float(Value(float('inf')))
        self.assertEqual(result, float('inf'), "Float inf cast != inf")

        result = float(Value('Infinity'))
        self.assertEqual(result, float('inf'), "String 'Infinity' cast != inf")

        result = float(Value('-Infinity'))
        self.assertEqual(result, float('-inf'),
                         "String '-Infinity' cast != -inf")

        result = float(Value('inf'))
        self.assertEqual(result, 0, "String 'inf' cast == inf")

        result = float(Value('infinity'))
        self.assertEqual(result, 0, "String 'infinity' cast == inf")

        # Base change
        result = float(Value('0x424D'))
        self.assertEqual(result, 0x424D, "Hex not casted")

        result = float(Value('0b1010011'))
        self.assertEqual(result, 0b1010011, "Binary not casted")

        result = float(Value('0o52'))
        self.assertEqual(result, 0o52, 'Oct not casted')

        result = float(Value('0XaBcD'))
        self.assertEqual(result, 0xABCD, "Case sensitive hex cast")

        # Exponent
        result = float(Value('5e3'))
        self.assertEqual(result, 5000, "Exponent failed")

    def test_str(self):
        """Tests the __str__ method"""

        # str() will throw an error if type is not float

        result = str(Value('test'))
        self.assertEqual(result, 'test', "String modified")

        result = str(Value('3'))
        self.assertEqual(result, '3', "String '3' failed")

        result = str(Value(5))
        self.assertEqual(result, '5', "String '5' failed")

        result = str(Value("7.0"))
        self.assertEqual(result, '7.0', "String '7.0' failed")

        result = str(Value(13.0))
        self.assertEqual(result, '13', "Float 13.0 failed")

        result = str(Value(float('inf')))
        self.assertEqual(result, "Infinity", "Float inf failed")

        result = str(Value(float('-inf')))
        self.assertEqual(result, "-Infinity", "Float -inf failed")

        # result = str(Value(float('nan')))
        # self.assertEqual(result, 'NaN', "Float nan failed")

    def test_bool(self):
        """Tests the __bool__ method"""

        # bool() will throw an error if type is not bool

        # True
        result = bool(Value("value"))
        self.assertEqual(result, True, "String 'value' not True")

        result = bool(Value("true"))
        self.assertEqual(result, True, "String 'true' not True")

        result = bool(Value(True))
        self.assertEqual(result, True, "Bool True not True")

        result = bool(Value(3))
        self.assertEqual(result, True, "Int 3 not True")

        result = bool(Value(5.0))
        self.assertEqual(result, True, "Float 5.0 not True")

        result = bool(Value("NaN"))
        self.assertEqual(result, True, "String 'NaN' not True")

        result = bool(Value("nan"))
        self.assertEqual(result, True, "String 'nan' not True")

        result = bool(Value(float('inf')))
        self.assertEqual(result, True, "Float inf not True")

        result = bool(Value(float('-inf')))
        self.assertEqual(result, True, "Float -inf not True")

        # False
        result = bool(Value("false"))
        self.assertEqual(result, False, "String 'false' not False")

        result = bool(Value("FaLsE"))
        self.assertEqual(result, False, "String 'FaLsE' not False")

        result = bool(Value("0"))
        self.assertEqual(result, False, "String '0' not False")

        result = bool(Value(float('nan')))
        self.assertEqual(result, False, "Float nan not False")

    def test_add(self):
        """Tests the __add__ method"""

        # Value doesn't handle handle parsing the added value
        # The added value must have a working float() method

        # Integers
        result = Value(3) + 5
        self.assertEqual(result, 8, "Value(3) + 5 failed")

        result = Value('7') + 13
        self.assertEqual(result, 20, "Value('7') + 5 failed")

        # Decimals
        result = Value(3.14) + 1
        self.assertAlmostEqual(result, 4.14, 7, "Value(3.14) + 1 failed")

        result = Value('9.81') + 0.09
        self.assertAlmostEqual(result, 9.9, 7,
                               "Value('9.81') + 0.09 failed")

        # Strings
        result = Value("test") + 3
        self.assertEqual(result, 3, 'Value("test") + 3 failed')

        result = Value("inf") + 5
        self.assertEqual(result, 5, 'Value("inf") + 5 failed')

        result = Value("+Infinity") + 7
        self.assertEqual(result, float('inf'), 'Value("Infinity") + 7 failed')

        # Value
        result = Value('2') + Value('3')
        self.assertEqual(result, 5, "Value('2') + Value('3') failed")

    def test_radd(self):
        """Tests the __radd__ method"""

        # Integers
        result = 5 + Value(3)
        self.assertEqual(result, 8, "5 + Value(3) failed")

        result = 13 + Value('7')
        self.assertEqual(result, 20, "13 + Value('7') failed")

        # Decimals
        result = 1 + Value(3.14)
        self.assertAlmostEqual(result, 4.14, 7, "1 + Value(3.14) failed")

        result = 0.09 + Value('9.81')
        self.assertAlmostEqual(result, 9.9, 7,
                               "0.09 + Value('9.81') failed")

        # Strings
        result = 3 + Value("test")
        self.assertEqual(result, 3, '3 + Value("test") failed')

        result = 5 + Value("inf")
        self.assertEqual(result, 5, '5 + Value("inf") failed')

        result = 7 + Value("+Infinity")
        self.assertEqual(result, float('inf'), '7 + Value("+Infinity") failed')

    def test_sub(self):
        """Tests the __sub__ method"""

        # Integers
        result = Value(3) - 5
        self.assertEqual(result, -2, "Value(3) - 5 failed")

        result = Value('7') - 13
        self.assertEqual(result, -6, "Value('7') - 5 failed")

        # Decimals
        result = Value(3.14) - 1
        self.assertAlmostEqual(result, 2.14, 7, "Value(3.14) - 1 failed")

        result = Value('9.81') - 0.09
        self.assertAlmostEqual(result, 9.72, 7,
                               "Value('9.81') - 0.09 failed")

        # Strings
        result = Value("test") - 3
        self.assertEqual(result, -3, 'Value("test") - 3 failed')

        result = Value("inf") - 5
        self.assertEqual(result, -5, 'Value("inf") - 5 failed')

        result = Value("+Infinity") - 7
        self.assertEqual(result, float('inf'), 'Value("Infinity") - 7 failed')

        # Value
        result = Value('2') - Value('3')
        self.assertEqual(result, -1, "Value('2') - Value('3') failed")

    def test_rsub(self):
        """Tests the __rsub__ method"""

        # Integers
        result = 5 - Value(3)
        self.assertEqual(result, 2, "5 - Value(3) failed")

        result = 13 - Value('7')
        self.assertEqual(result, 6, "13 - Value('7') failed")

        # Decimals
        result = 1 - Value(3.14)
        self.assertAlmostEqual(result, -2.14, 7, "1 - Value(3.14) failed")

        result = 0.09 - Value('9.81')
        self.assertAlmostEqual(result, -9.72, 7,
                               "0.09 - Value('9.81') failed")

        # Strings
        result = 3 - Value("test")
        self.assertEqual(result, 3, '3 - Value("test") failed')

        result = 5 - Value("inf")
        self.assertEqual(result, 5, '5 - Value("inf") failed')

        result = 7 - Value("+Infinity")
        self.assertEqual(result, float('-inf'),
                         '7 - Value("+Infinity") failed')

    def test_mul(self):
        """Tests the __mul__ method"""

        # Integers
        result = Value(3) * 5
        self.assertEqual(result, 15, "Value(3) * 5 failed")

        result = Value('7') * 13
        self.assertEqual(result, 91, "Value('7') * 5 failed")

        # Decimals
        result = Value(3.14) * 1
        self.assertEqual(result, 3.14, "Value(3.14) * 2 failed")

        result = Value('9.81') * 0.09
        self.assertAlmostEqual(result, 0.8829, 7,
                               "Value('9.81') * 0.09 failed")

        # Strings
        result = Value("test") * 3
        self.assertEqual(result, 0, 'Value("test") * 3 failed')

        result = Value("inf") * 5
        self.assertEqual(result, 0, 'Value("inf") * 5 failed')

        result = Value("+Infinity") * 7
        self.assertEqual(result, float('inf'), 'Value("Infinity") * 7 failed')

        # Value
        result = Value('2') * Value('3')
        self.assertEqual(result, 6, "Value('2') * Value('3') failed")

    def test_rmul(self):
        """Tests the __rmul__ method"""

        # Integers
        result = 5 * Value(3)
        self.assertEqual(result, 15, "5 * Value(3) failed")

        result = 13 * Value('7')
        self.assertEqual(result, 91, "13 * Value('7') failed")

        # Decimals
        result = 1 * Value(3.14)
        self.assertEqual(result, 3.14, "1 * Value(3.14) failed")

        result = 0.09 * Value('9.81')
        self.assertAlmostEqual(result, 0.8829, 7,
                               "0.09 * Value('9.81') failed")

        # Strings
        result = 3 * Value("test")
        self.assertEqual(result, 0, '3 0 Value("test") failed')

        result = 5 * Value("inf")
        self.assertEqual(result, 0, '5 * Value("inf") failed')

        result = 7 * Value("+Infinity")
        self.assertEqual(result, float('inf'), '7 * Value("+Infinity") failed')

    def test_truediv(self):
        """Tests the __truediv__ method"""

        # Integers
        result = Value(3) / 5
        self.assertEqual(result, 0.6, "Value(3) / 5 failed")

        result = Value('7') / 13
        self.assertEqual(result, 7/13, "Value('7') / 5 failed")

        # Decimals
        result = Value(3.14) / 1
        self.assertEqual(result, 3.14, "Value(3.14) / 1 failed")

        result = Value('9.81') / 0.09
        self.assertAlmostEqual(result, 109, 7,
                               "Value('9.81') / 0.09 failed")

        # Strings
        result = Value("test") / 3
        self.assertEqual(result, 0, 'Value("test") + 3 failed')

        result = Value("inf") / 5
        self.assertEqual(result, 0, 'Value("inf") + 5 failed')

        result = Value("+Infinity") / 7
        self.assertEqual(result, float('inf'), 'Value("Infinity") + 7 failed')

        # Value
        result = Value('2') / Value('3')
        self.assertEqual(result, 2/3, "Value('2') / Value('3') failed")

        # Division by Zero
        result = Value(5) / 0
        self.assertEqual(result, float('inf'), "Value(5) / 0 failed")

        result = Value('-7') / 0
        self.assertEqual(result, float('-inf'), "Value('-7') / 0 failed")

        result = Value(0) / 0
        self.assertIsInstance(result, Value)
        self.assertEqual(result, Value(float('nan')), "Value(0) / 0 failed")

    def test_rtruediv(self):
        """Tests the __radd__ method"""

        # Integers
        result = 5 / Value(3)
        self.assertEqual(result, 5/3, "5 / Value(3) failed")

        result = 13 / Value('7')
        self.assertEqual(result, 13/7, "13 / Value('7') failed")

        # Decimals
        result = 1 / Value(3.14)
        self.assertEqual(result, 1/3.14, "1 / Value(3.14) failed")

        result = 0.09 / Value('9.81')
        self.assertAlmostEqual(result, 0.09/9.81, 7,
                               "0.09 / Value('9.81') failed")

        # Strings
        result = 3 / Value("test")
        self.assertEqual(result, float('inf'), '3 / Value("test") failed')

        result = 5 / Value("inf")
        self.assertEqual(result, float('inf'), '5 + Value("inf") failed')

        result = 7 / Value("+Infinity")
        self.assertEqual(result, 0, '7 / Value("+Infinity") failed')

        # Division by Zero
        result = 5 / Value(0)
        self.assertEqual(result, float('inf'), "5 / Value(0) failed")

        result = -7 / Value('0')
        self.assertEqual(result, float('-inf'), "-7 / Value('0') failed")

        result = 0 / Value(0)
        self.assertIsInstance(
            result, Value, "0 / Value(0) should be NaN Value")
        self.assertEqual(result, Value(float('nan')), "0 / Value(0) failed")

    def test_mod(self):
        """Tests the __sub__ method"""

        # Integers
        result = Value(3) % 5
        self.assertEqual(result, 3, "Value(3) % 5 failed")

        result = Value('13') % 7
        self.assertEqual(result, 6, "Value('13') % 7 failed")

        # Decimals
        result = Value(3.14) % 1
        self.assertAlmostEqual(result, 0.14, 7, "Value(3.14) % 1 failed")

        result = Value('9.81') % 0.09
        self.assertEqual(result, 9.81 % 0.09,
                         "Value('9.81') % 0.09 failed")

        # Strings
        result = Value("test") % 3
        self.assertEqual(result, 0, 'Value("test") % 3 failed')

        result = Value("inf") % 5
        self.assertEqual(result, 0, 'Value("inf") % 5 failed')

        result = Value("+Infinity") % 7
        self.assertIsInstance(
            result, Value, "Value('+Infinity') % 7 should be NaN Value")
        self.assertEqual(result, Value(float('nan')),
                         'Value("+Infinity") % 7 failed')

        # Value
        result = Value('2') % Value('3')
        self.assertEqual(result, 2, "Value('2') % Value('3') failed")

    def test_rmod(self):
        """Tests the __rsub__ method"""

        # Integers
        result = 5 % Value(3)
        self.assertEqual(result, 2, "5 % Value(3) failed")

        result = 13 % Value('7')
        self.assertEqual(result, 1, "13 % Value('7') failed")

        # Decimals
        result = 1 % Value(3.14)
        self.assertEqual(result, 1, "1 % Value(3.14) failed")

        result = 0.09 % Value('9.81')
        self.assertEqual(result, 0.09,
                         "0.09 % Value('9.81') failed")

        # Strings
        result = 3 % Value("test")
        self.assertIsInstance(
            result, Value, "3 % Value('test') should be NaN Value")
        self.assertEqual(result, Value(float('nan')),
                         '3 % Value("test") failed')

        result = 5 % Value("inf")
        self.assertIsInstance(
            result, Value, "5 % Value('inf') should be NaN Value")
        self.assertEqual(result, Value(float('nan')),
                         '5 % Value("inf") failed')

        result = 7 % Value("+Infinity")
        self.assertEqual(result, 7,
                         '7 % Value("+Infinity") failed')


def main():
    """Runs the tests"""
    ValueTests().run()


if __name__ == '__main__':
    main()
