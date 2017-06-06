import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_general_case(self):
        """
        Test num_buses. Returns number of minimum buses required to
        transport n people.
        """

        actual1 = a1.num_buses(75)
        expected1 = 1
        
        actual2 = a1.num_buses(150)
        expected2 = 3
        
        actual3 = a1.num_buses(235)
        expected3 = 4
        
        actual4 = a1.num_buses(-3)
        expected4 = 0
        
        self.assertEqual(actual1, expected1)
        self.assertEqual(actual2, expected2)
        self.assertEqual(actual3, expected3)
        self.assertEqual(actual4, expected4)


if __name__ == '__main__':
    unittest.main(exit=False)
