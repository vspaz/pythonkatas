from datastructures.stack.stack import StackList


OPERATIONS = {
    "*": lambda x, y: x * y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y,
    "+": lambda x, y: x + y,
}


def postfix_calculator(expression):
    tokens = expression.split()
    stack = StackList()

    for token in tokens:
        if token.isnumeric():
            stack.push(float(token))
        elif token in OPERATIONS:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.push(OPERATIONS[token](num2, num1))
        else:
            raise RuntimeError("Invalid token!")
    return stack.pop()
