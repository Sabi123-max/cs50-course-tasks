import random


def main():
    level = get_level()
    score = 0
    tries = 0

    while True:
        index = 0
        x = generate_integer(level)
        y = generate_integer(level)
        r = input(f"{x} + {y} = ")
        result = x + y
        while True:
            if r.isdigit():
                if result == int(r):
                    score = score + 1
                    break
                else:
                    print("EEE")
                    index = index + 1
                    if index == 3:
                        print(f"{x} + {y} = {result}")
                        index = 0
                        break
                    else:
                        r = input(f"{x} + {y} = ")
            else:
                    print("EEE")
                    index = index + 1
                    if index == 3:
                        print(f"{x} + {y} = {result}")
                        index = 0
                        break
                    else:
                        r = input(f"{x} + {y} = ")

        tries = tries + 1
        if tries == 10:
            break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
