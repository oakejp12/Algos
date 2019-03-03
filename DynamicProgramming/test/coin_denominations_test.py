import DynamicProgramming.coin_denominations as cd
import unittest

class Test_TestIsChangePossibleGivenCoins(unittest.TestCase):
    def test_should_make_change(self):
        C = [1, 3, 2, 4]
        self.assertTrue(cd.is_change_possible(C, 5))

    def test_should_not_make_exact_change(self):
        C = [5, 10]
        self.assertFalse(cd.is_change_possible(C, 12))

    def test_large_test_should_make_change(self):
        C = [1, 14, 5, 2, 100, 4, 10, 8]
        self.assertTrue(cd.is_change_possible(C, 18))

if __name__ == "__main__":
    unittest.main()    