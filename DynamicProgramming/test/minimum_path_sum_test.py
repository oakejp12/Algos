import DynamicProgramming.minimum_path_sum as min_path
import unittest


class Test_TestMinPathSum(unittest.TestCase):
    def test_should_get_min_path(self):
        A = [[1, 3, 1],
             [1, 5, 1],
             [4, 2, 1]]

        D = min_path.calc_min_path_sum(A, 3, 3)

        min_path_sum = 7  # 1 -> 3 -> 1 -> 1 -> 1

        self.assertEqual(
            min_path_sum, min_path.backtrack_calc_min_sum(A, D, 3, 3))


if __name__ == "__main__":
    unittest.main()
