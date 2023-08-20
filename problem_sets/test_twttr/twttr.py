def main():
    word = input("Please talk to me.\n")
    output = shorten(word)
    print(output)

def shorten(word):
    output = ""
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o" ,"u"]
    output = [output.join(str(char)) for char in word  if char not in vowels]
    return "".join(output)


if __name__ == "__main__":
    main()


