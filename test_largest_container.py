import unittest
from largest_container import largest_container


class TestLargestContainer(unittest.TestCase):
    def test_increasing_heights(self):
        heights = [1, 2, 3, 4, 5]
        result = largest_container(heights)
        self.assertEqual(result, 6)

    def test_decreasing_heights(self):
        heights = [5, 4, 3, 2, 1]
        result = largest_container(heights)
        self.assertEqual(result, 6)

    def test_mixed_heights(self):
        heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        result = largest_container(heights)
        self.assertEqual(result, 49)

    def test_single_element(self):
        heights = [5]
        result = largest_container(heights)
        self.assertEqual(result, 0)

    def test_two_elements(self):
        heights = [1, 2]
        result = largest_container(heights)
        self.assertEqual(result, 1)

    def test_empty_list(self):
        heights = []
        result = largest_container(heights)
        self.assertEqual(result, 0)

    def test_all_elements_same(self):
        heights = [5, 5, 5, 5]
        result = largest_container(heights)
        self.assertEqual(result, 15)

    def test_large_numbers(self):
        heights = [1000, 2000, 3000, 4000]
        result = largest_container(heights)
        self.assertEqual(result, 4000)


if __name__ == '__main__':
    unittest.main()
