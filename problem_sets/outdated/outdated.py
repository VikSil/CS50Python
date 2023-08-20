def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        olddate = input("Date: ").strip()

        try:
            if olddate.find("/")>0:
                month,day,year=olddate.split("/")
                if checkdate(day,month):
                    break
            elif olddate.find(",")>0:
                month,day,year=olddate.split(" ")
                month = str(months.index(month)+1)
                day = day.replace(",","")
                if checkdate(day,month):
                    break

            else:
                continue

        except:
            continue


    print(f"{year}-{int(month):02}-{int(day):02}")


def checkdate(days,month):
    if int(days)<32 and int(month)<13:
        return True
    return False


main()