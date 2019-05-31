import String.valid_parens as sol
import unittest


class Test_TestValidParentheses(unittest.TestCase):

    def test_is_valid(self):
        parensStr = '[]{()}[]'
        self.assertEquals(True, sol.isValid(parensStr))

    def test_is_not_valid(self):
        parensStr = '[}]'
        self.assertEqual(False, sol.isValid(parensStr))

    def test_not_valid_empty_stack(self):
        parensStr = '[]]{]'
        self.assertEqual(False, sol.isValid(parensStr))

if __name__ == "__main__":
    unittest.main()
