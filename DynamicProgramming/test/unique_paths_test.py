import DynamicProgramming.unique_paths as uq
import unittest


class Test_TestUniquePaths(unittest.TestCase):
    def test_unique_path_small(self):
        m = 3
        n = 2
        output = 3
        self.assertEquals(output, uq.unique_paths(m, n))

    def test_unique_path_med(self):
        m = 7
        n = 3
        output = 28
        self.assertEquals(uq.unique_paths(m, n), output)

    def test_unique_path_none(self):
        m = 0
        n = 0
        output = 0
        self.assertEquals(uq.unique_paths(m, n), output)


if __name__ == "__main__":
    unittest.main()
