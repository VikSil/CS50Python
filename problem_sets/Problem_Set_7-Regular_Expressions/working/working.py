import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        match = re.search(r"(.+) ([A|P]M) to (.+)([A|P]M)", s)

        start = convert2(match.group(1),match.group(2))
        finish = convert2(match.group(3),match.group(4))

        return(f"{start} to {finish}")
    except:
        raise ValueError("Wrong value!")

def convert2(sf, amp):
    #if there is a colon in the string
    try:
        match = re.search(r"(.+):(.+)",sf)
        if match:
            hours = valid_hours(match.group(1), amp)
            minutes = valid_minute(match.group(2).strip())
            return(f"{hours}:{minutes}")
    #if there is no colon in the string
        else:
            hours = valid_hours(sf, amp)
            return(f"{hours}:00")
    except:
        raise ValueError("Wrong value!")

def valid_hours(h, amp):
    try:
        if amp == "AM":
            if 0 <= int(h) <= 11:
                return f"{int(h):02}"
            elif int(h) == 12:
                return "00"
            else:
                raise ValueError("Wrong value!")
        else:
            if int(h) == 12:
                return "12"
            else:
                return str(int(h)+12)

    except:
        raise ValueError("Wrong value!")

def valid_minute(m):
    try:
        if 0 <= int(m) <= 59:
                return (m)
        else:
            raise ValueError("Wrong value!")
    except:
        raise ValueError("Wrong value!")


if __name__ == "__main__":
    main()