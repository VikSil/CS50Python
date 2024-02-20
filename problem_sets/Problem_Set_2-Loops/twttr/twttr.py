def main():
    text = input("Please talk to me.\n")
    output = ""
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o" ,"u"]
    output = [output.join(str(char)) for char in text  if char not in vowels]
    print("".join(output))


main()

