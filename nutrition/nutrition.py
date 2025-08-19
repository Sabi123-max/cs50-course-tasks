fruit = input("Fruit: ")
cal = {
    "apple": 130,
    "Avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew Melon": 50,
    "Kiwifruit": 90,
    "lemon": 15,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
    "lime":20


}
for keys in cal:
    if fruit == keys:
        print(cal[keys])
