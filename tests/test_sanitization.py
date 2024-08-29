"""
Unit tests for sanitization

TODO Test for quoting text containg newlines
"""

import sys
import unittest

sys.path.insert(0, '../')
try:
    from sb3topy import sanitizer
except ImportError:
    from src.sb3topy import sanitizer


class SanitizationTests(unittest.TestCase):
    """Contains tests for sanitization"""

    def test_clean_identifier(self):
        """Tests the clean_identifier method"""
        with self.assertLogs() as logs:  # In 3.10, assertNoLogs better
            result = sanitizer.clean_identifier(
                "what!@#$%^&*()_is_up:\"{}|<>?,./-=")
            self.assertEqual(result, "what_is_up", "Symbols not stripped")

            result = sanitizer.clean_identifier("1234hello_world")
            self.assertEqual(result, "hello_world",
                             "Preluding digits not stripped")

            result = sanitizer.clean_identifier("123bob45678")
            self.assertEqual(result, "bob45678", "Trailing digits stripped")

            result = sanitizer.clean_identifier("__init__")
            self.assertEqual(result, "init", "Double underscores not stripped")

            result = sanitizer.clean_identifier("__main___")
            self.assertEqual(
                result, "main_", "Triple undescore stripped completely")

            result = sanitizer.clean_identifier("_test")
            self.assertEqual(
                result, "test", "Preluding underscore not stripped")

            result = sanitizer.clean_identifier(
                "custom block str %s num %n bool %b")
            self.assertEqual(result, "customblockstrnumbool",
                             "Prototype pcodes not stripped")

            self.assertFalse(logs.output, "Message logged")

            result = sanitizer.clean_identifier("1", "default1")
            self.assertEqual(result, "default1")
            self.assertEqual(len(logs.output), 1)

            result = sanitizer.clean_identifier("", "default2")
            self.assertEqual(result, "default2")
            self.assertEqual(len(logs.output), 2)

    def test_quote_string(self):
        """Tests the quote_string method"""
        result = sanitizer.quote_string("hello world")
        self.assertEqual(result, '"hello world"', "String not quoted")

        result = sanitizer.quote_string("'hello world")
        self.assertEqual(result, '"\'hello world"', "Single quote escaped")

        result = sanitizer.quote_string('"hello world"')
        self.assertEqual(result, '"\\"hello world\\""',
                         "Double quote not escaped")

        result = sanitizer.quote_string(r'\n\t\\"\"')
        self.assertEqual(result, r'"\\n\\t\\\\\"\\\""',
                         "Slashes not escaped correctly")

        result = sanitizer.quote_string(None)
        self.assertEqual(result, '"None"', "None not quoted correctly")

        result = sanitizer.quote_string(1234)
        self.assertEqual(result, '"1234"', "Integer not quoted correctly")

        result = sanitizer.quote_string(3.14)
        self.assertEqual(result, '"3.14"', "Float not quoted correctly")

        # NOTE A trailing newline is removed. Is that bad?
        result = sanitizer.quote_string("hello\rworld\n\n")
        self.assertEqual(result, '"hello\\nworld\\n"',
                         "Newline not escaped correctly")

    def test_quote_field(self):
        """Tests the quote_field method"""
        result = sanitizer.quote_field("hello world")
        self.assertEqual(result, "'hello world'", "String not quoted")

        result = sanitizer.quote_field('"hello world')
        self.assertEqual(result, "'\"hello world'", "Double quote escaped")

        result = sanitizer.quote_field("'hello world'")
        self.assertEqual(result, "'\\'hello world\\''",
                         "Single quote not escaped")

        result = sanitizer.quote_field(r"\n\t\\'\'")
        self.assertEqual(result, r"'\\n\\t\\\\\'\\\''",
                         "Slashes not escaped correctly")

        result = sanitizer.quote_field(None)
        self.assertEqual(result, "'None'", "None not quoted correctly")

        result = sanitizer.quote_field(1234)
        self.assertEqual(result, "'1234'", "Integer not quoted correctly")

        result = sanitizer.quote_field(3.14)
        self.assertEqual(result, "'3.14'", "Float not quoted correctly")

        result = sanitizer.quote_field("hello\rworld\n\n")
        self.assertEqual(result, "'hello\\nworld\\n'",
                         "Newline not escaped correctly")

    def test_quote_number(self):
        """Tests the quote_number method"""
        result = sanitizer.quote_number(
            12345678901234567890123456789012345678901234567890)
        self.assertEqual(
            result, '12345678901234567890123456789012345678901234567890',
            "Long int quoted")

        result = sanitizer.quote_number(
            '12345678901234567890123456789012345678901234567890')
        self.assertEqual(
            result, '12345678901234567890123456789012345678901234567890',
            "Long int str quoted")

        result = sanitizer.quote_number(3.14)
        self.assertEqual(result, '3.14', "Float quoted")

        result = sanitizer.quote_number('3.14')
        self.assertEqual(result, '3.14', "Float str quoted")

        result = sanitizer.quote_number('5.12345678901234567890')
        self.assertEqual(result, '"5.12345678901234567890"',
                         "Long float str not quoted")

        result = sanitizer.quote_number('nan')
        self.assertEqual(result, '"nan"', "'nan' not quoted")

        result = sanitizer.quote_number('+inf')
        self.assertEqual(result, '"+inf"', "'+inf' not quoted")

        result = sanitizer.quote_number(False)
        self.assertEqual(result, '"False"', "False not quoted")

        result = sanitizer.quote_number(None)
        self.assertEqual(result, '"None"', "None not quoted")

        result = sanitizer.quote_number("hello world")
        self.assertEqual(result, '"hello world"', "String not quoted")

    def test_cast_number(self):
        """Tests the cast_number method"""
        result = sanitizer.cast_number(1, 1234)
        self.assertTrue(isinstance(result, int))
        self.assertEqual(result, 1)

        result = sanitizer.cast_number("2", 1234)
        self.assertTrue(isinstance(result, int))
        self.assertEqual(result, 2)

        result = sanitizer.cast_number("3.14", 1234)
        self.assertTrue(isinstance(result, float))
        self.assertEqual(result, 3.14)

        result = sanitizer.cast_number("four", 1234)
        self.assertTrue(isinstance(result, int))
        self.assertEqual(result, 1234)

        result = sanitizer.cast_number("nan", 1234)
        self.assertEqual(result, 1234)

        result = sanitizer.cast_number("inf", 1234)
        self.assertTrue(isinstance(result, float))
        self.assertEqual(result, float('inf'))

    def test_valid_md5ext(self):
        """Tests the valid_md5ext method"""
        result = sanitizer.valid_md5ext(
            '64068c5339c18213b3e5a4935af57313.wav')
        self.assertTrue(result, "Valid md5ext considered invalid")

        result = sanitizer.valid_md5ext(
            'd40e79085bc5f0ffa99d0f262b1c6054.mp3')
        self.assertTrue(result, "md5ext with .mp3 ext considered invalid")

        result = sanitizer.valid_md5ext(
            'C4261fdaddcf6a23dc7f966c7b956e12.exe')
        self.assertFalse(result, "Invalid md5ext considered invalid")

        result = sanitizer.valid_md5ext(
            'b7e6bcc672c8f709d3dc0de95978a50.png')
        self.assertFalse(result, "Short md5ext considered valid")

        result = sanitizer.valid_md5ext(
            '3b9e198becc6579bdc8b9ee372a537606.png')
        self.assertFalse(result, "Long md5ext considered valid")

        result = sanitizer.valid_md5ext(
            'b581e068825ed08ca9f01cc937784bd\\.png')
        self.assertFalse(result, "Slash allowed in md5ext")

        result = sanitizer.valid_md5ext(
            'b581e068825ed08ca9f01cc937784bd/.png')
        self.assertFalse(result, "Forward slash allowed in md5ext")

        result = sanitizer.valid_md5ext(
            'e4261fdaddcf6a23dc7f966c7b956e1.mpeg')
        self.assertFalse(result, "Long extension allowed in md5ext")

# TODO Additional sanitization unit tests


def main():
    """Runs the tests"""
    SanitizationTests().run()


if __name__ == '__main__':
    main()
