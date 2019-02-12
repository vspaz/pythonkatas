from datastructures.stack.stack import StackList


def is_brackets_balanced(astring):
    open_to_close_parens = {
        "{": "}",
        "(": ")",
        "[": "]",
    }

    stack = StackList()
    for char in astring:
        if char in open_to_close_parens:
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            top_element = stack.pop()
            if open_to_close_parens.get(top_element) != char:
                return False

    if stack.is_empty():
        return True
    return False
