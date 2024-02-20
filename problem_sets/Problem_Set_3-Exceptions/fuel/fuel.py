def main():
    while True:
        try:
            x, y= input("What does the gauge say?\n").split("/")
            if int(x)>int(y):
                continue
            else:
                fract = int(x)/int(y)
                break
        except (ValueError, ZeroDivisionError):
            print("try again")

    print_fract(fract)

def print_fract(fract):
    if 0.01>=fract:
        print("E")
    elif 0.99<=fract:
        print("F")
    else:
        print(str(int(round(fract*100,0)))+"%")

main()