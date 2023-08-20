import inflect

def main():

    names = []
    p = inflect.engine()

    while True:
        try:
            names.append(input("Name: "))
        except:
            break

    print("Adieu, adieu, to", p.join(names))

if __name__ == "__main__":
    main()