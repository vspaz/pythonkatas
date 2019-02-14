parens = {
    "(": ")",
    "{": "}",
    "[": "]",
}
closing_parens = {
    ")",
    "}",
    "]",
}


def is_balanced(astring):
    stack = []
    for char in astring:
        if char in parens:
            stack.append(char)
        elif char in closing_parens:
            if not stack:
                return False
            top = stack.pop()
            if parens[top] != char:
                return False
        else:
            continue
    return not stack


test_input = "([](){([])})"
if is_balanced(astring=test_input):
    print("Success")
else:
    print(len([i for i in test_input if i in parens or i in closing_parens]))
