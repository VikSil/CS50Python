def main():
    camel = input("What is the CamelCase variable name?\n")
    for char in camel:
        if char.isupper():
            print("_"+char.lower(),end="")
        else:
            print(char,end="")


main()