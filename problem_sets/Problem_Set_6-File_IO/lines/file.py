def main():
    greet = input("Greetings! \n").strip().lower()
    if greet.startswith("h"):
        if greet.startswith("hello"):
            print("$0")
        else:
            print("$20")
    else:
        print("$100")

#let's add a comment
#let's add a comment

main()