import sys, csv


def main():
    args = sys.argv

    if len(args) < 3:
        sys.exit("Too few command-line arguments")

    elif len(args) > 3:
        sys.exit("Too many command-line arguments")

    elif not args[1].endswith(".csv") or not args[2].endswith(".csv"):
        sys.exit("Not a .csv file")

    before = []
    after = []

    try:
        # print(args)
        with open(args[1]) as file:
            content = csv.DictReader(file)
            for row in content:
                before.append(row)
                after.append(
                    {
                        "first": row["name"].split(",")[1].strip(),
                        "last": row["name"].split(",")[0].strip(),
                        "house": row["house"].strip(),
                    }
                )

    except FileNotFoundError:
        sys.exit("File does not exist")

    with open(args[2], "w") as file:
        writer = csv.writer(file)
        writer.writerow(["first", "last", "house"])
        for i in after:
            writer.writerow([i["first"], i["last"], i["house"]])


if __name__ == "__main__":
    main()
