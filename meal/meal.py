def main():
    time = input("what time is it ").strip()
    result = convert(time)
    if 7 <= result <= 8:
        print("Breakfast time")
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")
    else:
        quit()

def convert(time):
    hour,minute = time.split(":")
    minute = float(minute)
    minute = minute / 60
    hour = float(hour)
    now = hour + minute
    return now


if __name__ == "__main__":
    main()
