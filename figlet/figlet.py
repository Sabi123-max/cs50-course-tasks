import pyfiglet
import sys
import random


f1 = ["slant", "rectangles", "alphabet"]
chois = random.choice(f1)

def main():
    try:

        if len(sys.argv) == 1:
            word = input("input: ")
            print(pyfiglet.figlet_format(word, font=chois))
        elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "-font":
            word = input("input: ")
            print(pyfiglet.figlet_format(word, font=sys.argv[2]))
        else:
             int("name")
    except:
         print("Invalid Usage")
         sys.exit(1)

def check(n):
     if n not in f1:
         f = pyfiglet.figlet_format("somthing",font=n)
         return f
     else:
         return True
main()


