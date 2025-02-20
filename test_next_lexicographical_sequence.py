import unittest
from next_lexicographical_sequence import next_lexicographical_sequence


class TestNextLexicographicalSequence(unittest.TestCase):
    def test_simple_case(self):
        s = "abc"
        result = next_lexicographical_sequence(s)
        self.assertEqual(result, "acb")

    def test_reverse_case(self):
        s = "cba"
        result = next_lexicographical_sequence(s)
        self.assertEqual(result, "abc")

    def test_single_character(self):
        s = "a"
        result = next_lexicographical_sequence(s)
        self.assertEqual(result, "a")

    def test_two_characters(self):
        s = "ab"
        result = next_lexicographical_sequence(s)
        self.assertEqual(result, "ba")

    def test_all_same_characters(self):
        s = "aaa"
        result = next_lexicographical_sequence(s)
        self.assertEqual(result, "aaa")

    def test_mixed_characters(self):
        s = "abdc"
        result = next_lexicographical_sequence(s)
        self.assertEqual(result, "acbd")

    def test_long_sequence(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        result = next_lexicographical_sequence(s)
        self.assertEqual(result, "abcdefghijklmnopqrstuvwxzy")

    def test_empty_string(self):
        s = ""
        result = next_lexicographical_sequence(s)
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
