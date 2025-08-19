def main():
    while True:
        try:
            check() == True
            result = round(x/y,2)
            final =  int(result * 100)

            fin(final)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
             break

def check():
    global x
    global y
    x,y = input("format: ").split("/")
    x = int(x)
    y = int(y)
    if x < 0 or y < 0 :
        return int("invalid")
    else:
        return True
def fin(final):
    if final > 100:
        return int("invalid")
    else:
        if final <= 1:
            print("E")
        elif final >= 99:
            print("F")
        else:
            print((f"{final}%"))
main()

