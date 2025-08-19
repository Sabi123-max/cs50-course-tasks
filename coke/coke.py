print("Amount Due:50")
owe = 50
while owe > 0:
    amount = int(input("insert coin: "))
    if amount == 5:
        owe = owe - 5
        if owe > 0:
            print(f"Amount due: {owe}")
    elif amount == 10:
        owe = owe - 10
        if owe > 0:
            print(f"Amount due: {owe}")

    elif amount == 25:
        owe = owe - 25
        if owe > 0:
            print(f"Amount due: {owe}")

    else:
        print(f"Amount due: {owe}")

owe = abs(owe)
print(f"Change Owed: {owe}")
