vow = ['a','e','i','o','u','A','E','I','O','U']
word = input("Input").strip()



for v in vow:
    if v in word:
        word = word.replace(v, "")

print(word)
