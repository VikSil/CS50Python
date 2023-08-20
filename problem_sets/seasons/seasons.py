from datetime import date
import inflect
import sys



def main():
    p = inflect.engine()

    date_in = input("Date of Birth:")
    birthdate = validate_date(date_in)
    minutes = date_diff(birthdate)

    print(p.number_to_words(minutes).capitalize().replace(" and", ""), "minutes")

def date_diff(date_in):
    try:
        diff = date.today() - date_in
        #td = date(2000,1,1)
        #diff = td - date_in
    except:
        sys.exit("Invalid date")

    return diff.days * 24 * 60

def validate_date(date_in):
    try:
        year,month,day = date_in.split("-")
        birthdate = date(int(year),int(month),int(day))
    except:
        sys.exit("Invalid date")

    if birthdate > date.today():
        sys.exit("Invalid date")

    return birthdate


if __name__ == "__main__":
    main()