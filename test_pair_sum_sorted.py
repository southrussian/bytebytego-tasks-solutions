import unittest
from pair_sum_sorted import pair_sum_sorted


class TestPairSumSorted(unittest.TestCase):
    def test_pair_found(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = pair_sum_sorted(nums, target)
        self.assertEqual(result, [0, 1])

    def test_pair_not_found(self):
        nums = [2, 7, 11, 15]
        target = 10
        result = pair_sum_sorted(nums, target)
        self.assertEqual(result, [])

    def test_empty_list(self):
        nums = []
        target = 5
        result = pair_sum_sorted(nums, target)
        self.assertEqual(result, [])

    def test_single_element(self):
        nums = [5]
        target = 5
        result = pair_sum_sorted(nums, target)
        self.assertEqual(result, [])

    def test_all_elements_same(self):
        nums = [5, 5, 5, 5]
        target = 10
        result = pair_sum_sorted(nums, target)
        self.assertEqual(result, [0, 3])

    def test_negative_numbers(self):
        nums = [-3, -1, 1, 2, 4, 5]
        target = 1
        result = pair_sum_sorted(nums, target)
        self.assertEqual(result, [0, 4])

    def test_large_numbers(self):
        nums = [1000, 2000, 3000, 4000]
        target = 5000
        result = pair_sum_sorted(nums, target)
        self.assertIn(result, [[1, 2], [0, 3]])


if __name__ == '__main__':
    unittest.main()
