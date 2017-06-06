import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """
    

    def test_divisors_example_1(self):
        """Test swap_k with [1, 2, 3, 4, 5, 6] and 2"""

        actual1 = a1.swap_k([1, 2, 3, 4, 5, 6], 2)
        expected1 = [5, 6, 3, 4, 1, 2]
        self.assertEqual(expected1, actual1)

    def test_divisors_example_2(self):
        """Test swap_k with [10, 13, 7, 9] and 2."""

        actual2 = a1.swap_k([10, 13, 7, 9], 2)
        expected2 = [7, 9, 10, 13]
        self.assertEqual(expected2, actual2)
    

if __name__ == '__main__':
    unittest.main(exit=False)
