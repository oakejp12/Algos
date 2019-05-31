'''
Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return
all possible letter combinations that the number could represent.

"23" -> ["ad", "ae", "af", "bd", "be", "bf", "cd", ...]
'''


def findStrings(integerStr: str, stringCombo: str, numsToLetter, combos: list):

    if integerStr == "":
        combos.append(stringCombo)
        return

    # The key idea here is that we're spawning the findStrings method
    # for each letter encountered and adding to it's own string combination
    # e.g. for "23", we'll spawn independent methods to concatenate strings
    #      on top of "a", "b", and "c"
    for char in numsToLetter[integerStr[0]]:
        findStrings(integerStr[1:], stringCombo + char, numsToLetter, combos)


def letterCombinations(integerStr: str) -> list:
    '''
    Returns all possible letter combinations from
    a dial pad given a string of numbers
    '''

    if not integerStr:
        return []

    # Initialize dial pad combinations to pull letters to numbers
    numsToLetter = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    combos = []
    findStrings(integerStr, "", numsToLetter, combos)

    return combos


if __name__ == "__main__":
    print(letterCombinations("23"))
