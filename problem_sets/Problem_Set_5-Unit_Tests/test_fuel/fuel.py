def main():
    while True:
        try:
            fraction = input("What does the gauge say?\n")
            fract = convert(fraction)
            break

        except (ValueError, ZeroDivisionError):
            print("try again")

    print(fract)

    print(gauge(fract))

def convert(fraction):
    try:
        x,y = fraction.split("/")
    except:
       raise ValueError("Wrong input!")

    try:
        int(x)/int(y)
    except (ZeroDivisionError):
        raise ZeroDivisionError("Division by Zero!")

    if int(x)>int(y):
        raise ValueError("X greater than Y!")
    else:
        return int(round(100*int(x)/int(y)))


def gauge(fract):
    if 1>=fract:
        return "E"
    elif 99<=fract:
        return "F"
    else:
        return (f"{fract}%")

if __name__ == "__main__":
    main()