import random

def main():

    while True:
        try:
            lvl = int(input("Level: "))
            if lvl > 0 :
                break
        except:
            continue

    rand = random.randint(1, lvl)
    guess = 0

    while guess != rand:
        try:
            guess = int(input("Guess: "))
            if guess < rand:
                print("Too small!")
            if guess > rand:
                print ("Too large!")
        except:
            continue
    print("Just right!")

if __name__ == "__main__":
    main()