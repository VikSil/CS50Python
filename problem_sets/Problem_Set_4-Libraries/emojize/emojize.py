import emoji

def main():
    text = input("Input: ")

    try:
        print("Output: " +emoji.emojize(text))
    except:
        print("I don't know that emoji")



if __name__ == "__main__":
    main()