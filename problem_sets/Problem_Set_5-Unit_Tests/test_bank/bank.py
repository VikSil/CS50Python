def main():
    greet = input("Greetings! \n").strip().lower()
    print(f"${value(greet)}")

def value(greeting):
    if greeting.startswith("h") or greeting.startswith("H") :
        if greeting.startswith("hello") or greeting.startswith("Hello"):
            return 0
        else:
            return 20
    else:
        return 100


if __name__ == "__main__":
    main()