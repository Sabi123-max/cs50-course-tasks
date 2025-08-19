import random


def main():
    while True:
        try:
            n = int(input("Level: "))
            check(n)
            result = random.randint(1,n)
            while check(n) == True:
                g = input("Guess: ")
                if g.isalpha() == True:
                    continue
                g = int(g)
                if g <= 0 :
                    continue
                else:
                    if result == g:
                        print("Just right!")
                        break
                    elif result < g:
                        print("Too large!")
                        continue
                    else:
                        print("Too small!")
                        continue
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def check(n):
    if n < 0:
        return int("name error")
    else:
        return True

def numch(n,g):
    if n != g:
        x = 1 / 0
        return x
    else:
        return True


main()
