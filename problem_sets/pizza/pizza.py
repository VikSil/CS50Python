import csv
from tabulate import tabulate
import sys


def main():
    args = sys.argv

    if len(args) < 2:
        sys.exit("Too few command-line arguments")

    elif len(args) > 2:
        sys.exit("Too many command-line arguments")

    elif not args[1].endswith(".csv"):
        sys.exit("Not a .csv file")

    try:
        table = []
        with open(args[1]) as file:
            content = csv.reader(file)
            # headers = content[0]
            for line in content:
                table.append(line)

    except FileNotFoundError:
        sys.exit("File does not exist")

    headers = table[0]
    print(tabulate(table[1:], headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
