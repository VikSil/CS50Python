def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    #Starts with at least 2 letters
    for char in plate[0:2]:
        if char.isdigit():
            return False

    #Between 6 and 2 characters
    if len(plate) <2 or len(plate) >6:
        return False

    #no numbers in the middle of the plate
    midnumber = False
    for char in plate[ : ]:
        if not char.isdigit():
            if midnumber:
                return False
        else:
            if not midnumber:
                midnumber = True

    #first number in the plate cannot be zero
    if plate.find("0") >0:
        if not plate[plate.find("0")-1].isdigit():
            return False

    #no periods, spaces, punctuation
    for char in plate[:]:
        if not char.isalnum():
            return False

    return True
main()