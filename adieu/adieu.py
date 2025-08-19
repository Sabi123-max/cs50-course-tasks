p=[]

while True:
    try:
        name = input("input:")
        p.append(name)
    except EOFError:
        print("")
        if len(p) == 0:
            break
        elif len(p) == 1:
            print(f"Adieu, adieu, to {p[0]}")
            break
        elif len(p) == 2:
            print(f"Adieu, adieu, to {p[0]} and {p[1]}")
            break
        else:
            n = len(p)
            k = n-1
            s = ', '.join(p[:k])
            print(f"Adieu, adieu, to {s}, and {p[-1]}")
            break
