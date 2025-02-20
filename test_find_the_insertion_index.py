import unittest
from find_the_insertion_index import find_the_insertion_index


class TestFindTheInsertionIndex(unittest.TestCase):
    def test_insert_at_beginning(self):
        nums = [2, 3, 5, 7]
        target = 1
        result = find_the_insertion_index(nums, target)
        self.assertEqual(result, 0)

    def test_insert_at_end(self):
        nums = [2, 3, 5, 7]
        target = 8
        result = find_the_insertion_index(nums, target)
        self.assertEqual(result, 4)

    def test_insert_in_middle(self):
        nums = [2, 3, 5, 7]
        target = 4
        result = find_the_insertion_index(nums, target)
        self.assertEqual(result, 2)

    def test_insert_existing_element(self):
        nums = [2, 3, 5, 7]
        target = 5
        result = find_the_insertion_index(nums, target)
        self.assertEqual(result, 2)

    def test_empty_list(self):
        nums = []
        target = 5
        result = find_the_insertion_index(nums, target)
        self.assertEqual(result, 0)

    def test_single_element_list(self):
        nums = [5]
        target = 3
        result = find_the_insertion_index(nums, target)
        self.assertEqual(result, 0)

    def test_single_element_list_greater(self):
        nums = [5]
        target = 7
        result = find_the_insertion_index(nums, target)
        self.assertEqual(result, 1)

    def test_all_elements_same(self):
        nums = [5, 5, 5, 5]
        target = 5
        result = find_the_insertion_index(nums, target)
        self.assertEqual(result, 0)

    def test_negative_numbers(self):
        nums = [-3, -1, 1, 2, 4, 5]
        target = 0
        result = find_the_insertion_index(nums, target)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()