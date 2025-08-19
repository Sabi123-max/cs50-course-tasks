def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    return alpha(s) and upper(s) and length(s)

def alpha(s):
    if s[:2].isalpha():
        return True

def upper(s):
    if s.isupper():
        return True
def length(s):
    ln = len(s)
    middle = ln / 2
    if  2 <= ln <= 6:
        if not special(s):
            return False
        if s.isalpha():
            return True
        if ln % 2 != 0:
            if s[middle].isdigit():
                return False
        for i,ch in enumerate(s):
             if ch.isdigit():
                   if ch == '0':
                        return False
                   return s[i:].isdigit()
        return True
    return False
def special(s):
    special = ['.','!',' ']
    for sa in special:
         if sa in s:
            return False
    return True
main()

