

def get_total():
    total = 0
    while True:
        user_input = input("Please enter some num: \n")
        try:
            total += float(user_input)
        except ValueError:
            break
    return total


if __name__ == "__main__":
    ret = get_total()
    print(ret)
