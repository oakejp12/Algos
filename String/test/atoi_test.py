import String.atoi as sol
import unittest


class Test_TestAtoi(unittest.TestCase):

    def test_atoi_valid(self):
        integerStr = '42'
        output = 42
        self.assertEquals(output, sol.atoi(integerStr))

    def test_atoi_with_words(self):
        integerStr = '4193 with words'
        output = 4193
        self.assertEqual(output, sol.atoi(integerStr))

    def test_atoi_with_overflow(self):
        integerStr = '-91283472332'
        output = -2147483648
        self.assertEqual(output, sol.atoi(integerStr))

if __name__ == "__main__":
    unittest.main()
