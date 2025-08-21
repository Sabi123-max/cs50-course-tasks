def main():
    word = input("inputL: ")
    print(shorten(word))
def shorten(word):
    l = ['a','e','i','o','u','A','E','I','O','U']
    for li in l:
        if li in word:
            word = word.replace(li,"")
    return word


if __name__ == "__main__":
    main()
