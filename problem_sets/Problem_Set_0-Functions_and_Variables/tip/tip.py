def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    output = float(d.replace("$",""))
    return (output)

def percent_to_float(p):
    output = float(p.replace("%",""))
    return(output/100)

main()