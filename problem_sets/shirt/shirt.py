import sys, csv
from PIL import Image
from PIL import ImageOps

def main():
    args = sys.argv
    ext = ['jpg', 'jpeg', 'png']

    if len(args) < 3:
        sys.exit("Too few command-line arguments")

    elif len(args) > 3:
        sys.exit("Too many command-line arguments")


    elif (args[1].split(".")[-1].lower() not in ext) or (args[2].split(".")[-1].lower() not in ext):
        sys.exit("Invalid input")

    elif args[1].split(".")[-1].lower() != args[2].split(".")[-1].lower():
        sys.exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
    except:
        sys.exit("Could not resize the shirt")

    try:
        origmuppet= Image.open(args[1])
        muppet= ImageOps.fit(origmuppet, size)
        muppet.paste(shirt, shirt)
        muppet.save(args[2])
    except:
        sys.exit("Something went wrong")

if __name__ == "__main__":
    main()
