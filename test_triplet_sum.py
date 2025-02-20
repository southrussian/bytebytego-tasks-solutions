import unittest
from triplet_sum import triplet_sum


class TestTripletSum(unittest.TestCase):
    def test_triplets_found(self):
        nums = [-1, 0, 1, 2, -1, -4]
        result = triplet_sum(nums)
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertCountEqual(result, expected)

    def test_no_triplets(self):
        nums = [1, 2, 3, 4, 5]
        result = triplet_sum(nums)
        self.assertEqual(result, [])

    def test_empty_list(self):
        nums = []
        result = triplet_sum(nums)
        self.assertEqual(result, [])

    def test_single_element(self):
        nums = [0]
        result = triplet_sum(nums)
        self.assertEqual(result, [])

    def test_all_elements_same(self):
        nums = [0, 0, 0, 0]
        result = triplet_sum(nums)
        self.assertEqual(result, [[0, 0, 0]])

    def test_negative_numbers(self):
        nums = [-3, -1, 1, 2, 4, 5]
        result = triplet_sum(nums)
        expected = [[-3, -1, 4], [-3, 1, 2]]
        self.assertCountEqual(result, expected)

    def test_large_numbers(self):
        nums = [-1000, -2000, 1000, 2000, 3000]
        result = triplet_sum(nums)
        expected = [[-2000, -1000, 3000]]
        self.assertCountEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
