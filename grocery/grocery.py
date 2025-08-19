
def main():
    global ls
    ls = {}
    while True:
        try:
            check()


        except EOFError:
            for v,k in sorted(ls.items()):
                print(f"{k} {v}")
            break
        except KeyError:
            pass



def check():
    global item
    item = input("")
    item = item.upper()

    if item not in ls:
        ls[item] = 1
        return ls
    else:
        ls[item] += 1
        return ls
main()
