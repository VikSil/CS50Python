def main():
    operation = input("what operation do you want to carry out?\n").strip().lower()
    x,y,z = operation.split(" ")
    match y:
        case "+":
            result = int(x)+int(z)
        case "-":
            result = int(x)-int(z)
        case "*":
            result = int(x)*int(z)
        case "/":
            result = int(x)/int(z)
    print(float(result))




main()