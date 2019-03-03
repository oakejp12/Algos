import DynamicProgramming.chain_matrix_multiply as cm
import unittest


class Test_TestChainMatrixMultiply(unittest.TestCase):
    def test_should_get_min_mults(self):
        M = [50, 20, 1, 10, 100]
        self.assertEqual(7000, cm.chain_matrix_multiply(M, 4))


if __name__ == "__main__":
    unittest.main()
