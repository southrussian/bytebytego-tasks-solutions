import unittest
from climbing_stairs import climbing_stairs


class TestClimbingStairs(unittest.TestCase):
    def test_one_step(self):
        n = 1
        result = climbing_stairs(n)
        self.assertEqual(result, 1)

    def test_two_steps(self):
        n = 2
        result = climbing_stairs(n)
        self.assertEqual(result, 2)

    def test_three_steps(self):
        n = 3
        result = climbing_stairs(n)
        self.assertEqual(result, 3)

    def test_four_steps(self):
        n = 4
        result = climbing_stairs(n)
        self.assertEqual(result, 5)

    def test_five_steps(self):
        n = 5
        result = climbing_stairs(n)
        self.assertEqual(result, 8)

    def test_large_number_of_steps(self):
        n = 10
        result = climbing_stairs(n)
        self.assertEqual(result, 89)

    def test_zero_steps(self):
        n = 0
        result = climbing_stairs(n)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
