import unittest

from threeSum import threeSum


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            threeSum([-1, 0, 1, 2, -1, -4]),
            [[-1, -1, 2], [-1, 0, 1]])

    def test_2(self):
        self.assertEqual(threeSum([0, 1, 1]),
                         [])

    def test_3(self):
        self.assertEqual(threeSum([0, 0, 0]), [[0, 0, 0]])


if __name__ == '__main__':
    unittest.main()
