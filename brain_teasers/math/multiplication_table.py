
def print_table(num1, num2):
    for i in range(1, num1 + 1):
        for j in range(1, num2 + 1):
            print("{:2}".format(i * j), end=" ")
        print()


if __name__ == "__main__":
    print_table(10, 10)
