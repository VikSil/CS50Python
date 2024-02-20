def main():
    due = 50
    change = 0

    while due > 0:
        coin = int(input("Insert Coin: "))
        if coin == 5 or coin == 10 or coin == 25:
            if due > coin:
                due = due - coin
                print ("Amount Due:", due)
            elif due == coin:
                due = 0
                change = 0
            else:
                change = coin - due
                due = 0
        else:
            print  ("Amount Due:", due)


    print ("Change Owed:", change)


if __name__ == "__main__":
    main()