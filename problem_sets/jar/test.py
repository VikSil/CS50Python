from jar import Jar


def main():
    blue = Jar(30)
    blue.deposit(3)
    print(blue.size)
    print("About to print cookies:")
    print(blue)


if __name__ == "__main__":
    main()