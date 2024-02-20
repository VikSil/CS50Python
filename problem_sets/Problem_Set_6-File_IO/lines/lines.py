import sys

def main():
    args = sys.argv

    if len(args)<2:
        sys.exit("Too few command-line arguments")

    elif len(args)>2:
        sys.exit("Too many command-line arguments")

    elif not args[1].endswith(".py"):
        sys.exit("Not a python file")

    try:
        with open(args[1]) as file:
            counter = 0
            for line in file:
                if not line.strip().startswith("#") and not line.lstrip() == "":
                    counter = counter+1

    except (FileNotFoundError):
        sys.exit("File does not exist")

    print(counter)


if __name__ == "__main__":
    main()