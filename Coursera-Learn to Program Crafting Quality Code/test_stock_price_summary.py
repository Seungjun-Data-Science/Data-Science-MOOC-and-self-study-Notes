import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def stock_price_summary_test_1(self):
        """Test stock_price_summary with
        [0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01].
        """

        actual1 = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected1 = (0.14, -0.17)
        self.assertEqual(expected1, actual1)

    def stock_price_summary_test2(self):
        """Test stock_price_summary with
        [-0.3, -0.23, 0.5, 0.02, -0.12, 0, 0.47]."""

        actual2 = a1.stock_price_summary([-0.3, -0.23, 0.5, 0.02, -0.12, 0, 0.47])
        expected2 = (0.99,-0.05)
        self.assertEqual(expected2, actual2)
        

if __name__ == '__main__':
    unittest.main(exit=False)
