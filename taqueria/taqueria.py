dict1 = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
global index
def main():
    index = 0
    while True:
        try:
            ch = check()
            val = total()
            print(ch)

        except ValueError:
            pass
        except EOFError:
            break
        else:

            val += index

            print(f"Total: ${val:.2f}")
            index = val



def check():
    global item
    item = input("Item: ").title()
    for key in dict1:
        if item == key:
            return key
    else:
        return int("error")
def total():
    value = dict1[item]
    return value

main()
