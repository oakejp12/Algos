import String.letter_combos as sol
import unittest


class Test_TestLetterCombinations(unittest.TestCase):

    def test_atoi_valid(self):
        integerStr = '23'
        outputLen = 9
        self.assertEquals(outputLen, len(sol.letterCombinations(integerStr)))

    def test_atoi_with_words(self):
        integerStr = '243'
        outputLen = 27
        self.assertEqual(outputLen, len(sol.letterCombinations(integerStr)))

if __name__ == "__main__":
    unittest.main()
