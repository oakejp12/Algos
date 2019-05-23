'''
Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return
all possible letter combinations that the number could represent.

"23" -> ["ad", "ae", "af", "bd", "be", "bf", "cd", ...]
'''


def letterCombinations(integerStr: str) -> list:

    if not integerStr:
        return []

    combos = []

    return combos

if __name__ == "__main__":
    print(letterCombinations("23"))
