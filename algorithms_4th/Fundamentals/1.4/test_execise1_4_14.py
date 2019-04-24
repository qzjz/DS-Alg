import random
import unittest

from execise1_4_14 import FourSumSolution


class TestFourSumSolution(unittest.TestCase):

    def test_four_sum(self):
        s = FourSumSolution()

        array, target = [-1, 0, 1, 2, -2, 3, -4, 5, -5, 7, 3], 0
        self.assertEqual(
            s.four_sum(array, target),
            [
                (-2, -1, 0, 3), (-5, -1, 1, 5), (-4, -2, -1, 7), (-4, -2, 1, 5),
                (-2, -1, 1, 2), (-4, -1, 2, 3), (-5, -4, 2, 7), (-4, 0, 1, 3),
                (-4, -1, 0, 5), (-5, 0, 2, 3), (-5, -2, 2, 5), (-5, -1, 3, 3),
                (-4, -2, 3, 3), (-5, -2, 0, 7)
            ]
        )
        array, target = [2, 1, -1, 5, 9, 7, 2, 0, 6, -1, -2, -4, 11, 10, -3], 5
        self.assertEqual(
            s.four_sum(array, target),
            [
                (-4, 0, 2, 7), (-4, -2, 1, 10), (-1, -1, 0, 7), (-2, -1, 1, 7),
                (-4, -2, 5, 6), (0, 1, 2, 2), (-3, -1, -1, 10), (-4, -2, 2, 9),
                (-4, -1, 0, 10), (-2, 0, 2, 5), (-3, 0, 2, 6), (-4, -3, 2, 10),
                (-1, 0, 1, 5), (-3, -2, 1, 9), (-3, 1, 2, 5), (-4, 1, 2, 6),
                (-4, -3, 5, 7), (-2, -1, -1, 9), (-3, -2, -1, 11), (-2, -1, 2, 6),
                (-4, -1, -1, 11), (-1, -1, 2, 5), (-2, 0, 1, 6), (-3, -1, 0, 9),
                (-3, -2, 0, 10), (-4, -1, 1, 9), (-3, 0, 1, 7), (-1, -1, 1, 6),
                (-4, -3, 1, 11), (-4, -2, 0, 11), (-4, 2, 2, 5), (-3, -1, 2, 7)]
        )

        array, target = [8, 3, 2, 4, 1, 0, -1, -2, -5, 9, 11, 0], 6
        self.assertEqual(
            s.four_sum(array, target),
            [(-5, -2, 2, 11), (-5, 0, 3, 8), (-5, 1, 2, 8), (-2, -1, 1, 8),
                (0, 0, 2, 4), (-5, -1, 3, 9), (-2, 1, 3, 4), (0, 1, 2, 3),
                (-2, 0, 0, 8), (-1, 0, 3, 4), (-1, 1, 2, 4), (-5, -1, 4, 8),
                (-5, 0, 2, 9), (-2, -1, 0, 9), (-5, -2, 4, 9), (-5, -1, 1, 11),
                (-5, 0, 0, 11)
             ]
        )


if __name__ == "__main__":
    unittest.main()
