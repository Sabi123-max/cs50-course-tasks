def main():
    exp = input("Expression: ").split()
    result = operation(exp)
    if result is not None:
        print(result)


def operation(n):
    n1 = float(n[0])
    n3 = float(n[-1])
    if n[1] == "+":
        return (n1+n3)
    elif n[1] == "-":
        return (n1-n3)
    elif n[1] == "*":
        return (n1*n3)
    elif n[1] == "/":
        if n3 != 0:
            return round(n1/n3, 1)
        else:
            print("z can never be zero")
            return None
    else:
        print("upload properly")
        return None

main()
