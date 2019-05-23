'''
Implement atoi
'''


def atoi(integerStr: str) -> int:

    if not integerStr:
        return 0

    # Strip all leading whitespace
    # characters for the string
    integerStr = integerStr.lstrip()

    integer = 0
    operand = ""
    count = 0

    for char in integerStr:
        if count == 0:
            if isAlphaCharacter(char):
                return 0
            elif isOperandCharacter(char):
                operand = char
            elif char.isdigit():
                integer = (ord(char) - ord('0'))
            else:
                # The value is something freaky....
                return 0

            # Make sure to get out of counting the first char
            count += 1
        else:
            if char.isdigit():
                integer = (integer * 10) + (ord(char) - ord('0'))
            else:
                break

    # Convert integer based on operand
    if operand == '-':
        integer = -(integer)

    return getIntegerWithinBounds(integer)


def isAlphaCharacter(charz: str) -> bool:
    uniCodePoint = ord(charz)
    return uniCodePoint >= 65 and uniCodePoint <= 122


def isNumericCharacter(charz: str) -> bool:
    uniCodePoint = ord(charz)
    return uniCodePoint >= 48 and uniCodePoint <= 57


def isOperandCharacter(str: str) -> bool:
    '''
    We're only considering a (-) or a (+)
    '''
    uniCodePoint = ord(str)
    return uniCodePoint == 43 or uniCodePoint == 45


def getIntegerWithinBounds(integer: int) -> int:
    if integer < pow(-2, 31):
        return pow(-2, 31)
    elif integer > pow(2, 31) - 1:
        return pow(2, 31) - 1
    else:
        return integer


if __name__ == "__main__":

    print(atoi("42"))
