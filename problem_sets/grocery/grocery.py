def main():
    groceries = {}

    while True:
        try:
            item = input().strip().upper()

            if item not in groceries:
                groceries[item] = 1
            else:
                groceries[item] = groceries[item] +1

        except EOFError:
            break


    for key,value in sorted(groceries.items()):
        print(value, key)




main()