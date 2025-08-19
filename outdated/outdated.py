def main():
    list = [
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
        try:
            n = input("Date:")
            if n[0].isalpha() == True:
                formatcheck(n)
            elif n[0].isalpha() == False:
                checkcheck(n)
            else:
                n = int("error")
            n = n.replace("/"," ").replace(",","").split()
            if n[0].isalpha() == True:
                month = n[0]
                day = int(n[1])
                year = n[2]


            elif n[1].isdigit() == True:
                 month = int(n[0])
                 day = int(n[1])
                 year = n[2]

                 monthcheck(month)
            else:
                month = int("sabik")

            daycheck(day)
            for i,x in enumerate(list):
                if month == x:
                    month = i + 1
                    break
            print(f"{year}-{month:02}-{day:02}")
            break

        except ValueError:
            pass
def formatcheck(n):
    if "," in n:
        if n[0].isalpha() == True:
            return True
        else:
            return int("error")
    else:
        return int("error")

def checkcheck(n):
    if "/" in n:
        if n[0].isalpha() == False:
            return True
        else:
            return int("error")
    else:
        return int("error")
def monthcheck(month):
    if month > 12:
        month  == int("sabik")
        return month
def daycheck(day):
    if day>31:
        day == int("sabik")
        return day





main()
