import DynamicProgramming.contiguous_subsequence as cs
import unittest

class Test_TestContiguousSubsequence(unittest.TestCase):
    def test_contiguous_subsequence(self):
        A = [5, 15, -30, 10, -5, 40, 10]
        L = [10, -5, 40, 10]
        self.assertEqual(L, cs.max_sum_of_sequence(A))

    def test_contiguous_subsequenceLarger(self):
        A = [5, -30, -1000, 1000, -20, -900, 15, 950, 75, -5, -200, 1000]
        L = [1000, -20, -900, 15, 950, 75, -5, -200, 1000]
        self.assertEqual(L, cs.max_sum_of_sequence(A))

    def test_contiguous_subsequenceEmpty(self):
        self.assertEqual([], cs.max_sum_of_sequence([]))


if __name__ == "__main__":
    unittest.main()    


