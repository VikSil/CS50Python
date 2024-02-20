def main():
    time = input("What time is it? ").strip().lower()
    dectime = convert(time)

    if 7<= dectime <=8:
        print("breakfast time")
    elif 12<=dectime <= 13:
        print("lunch time")
    elif 18<=dectime <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    dectime = float(hours)+float(minutes)/60
    return dectime


if __name__ == "__main__":
    main()