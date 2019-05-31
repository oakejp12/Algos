'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

'''


def isValid(parens: str) -> bool:
    '''
    Returns true is the provided parentheses
    are valid.
    '''

    composite = {
        ']': '[',
        '}': '{',
        ')': '('
    }

    # Push to the stack on an open parens
    # On close parens, check if top of stack matches
    #   and fail if not, pop if so
    stack = []

    for paren in parens:
        if paren == '[' or paren == '(' or paren == '{':
            stack.append(paren)
        elif len(stack) == 0:
            # If there's nothing to pop, then there's no
            # matching parentheses
            return False
        else:
            topParen = stack[-1]
            compositeParen = composite[paren]
            if topParen != compositeParen:
                return False
            else:
                stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    isValid('[}]')
