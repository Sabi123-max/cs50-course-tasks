def main():
    name = input("CamelName: ").strip().replace(" ", "")
    iterate(name)

def iterate(str):
    for s in str:
        s = check(s)
        print(s,end="")

def check(s):
    if s.isupper():
        s = "_" + s
        s = s.lower()
    return s





main()
