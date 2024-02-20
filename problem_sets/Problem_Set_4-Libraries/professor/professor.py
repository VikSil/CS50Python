import random


def main():
    lvl = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        score = score + problem (x,y)
    print("Score:", score)

def get_level():
    while True:
        try:
            lvl = int(input("Level:"))
            if 1<= lvl <=3:
                return lvl
        except:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    if level == 2:
        return random.randint(10,99)
    if level == 3:
        return random.randint(100,999)


def problem(x,y):
    answer = x+y
    try:
        for _ in range(3):
            answ = int(input(f"{x} + {y} = "))
            if answ == answer:
                return 1
            else:
                print("EEE")
                continue
        print(str(x),"+",str(y),"=",answer)
        return 0
    except:
        return 0

if __name__ == "__main__":
    main()