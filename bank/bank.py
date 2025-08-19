def main():
    greet = input("Greeting:").lower().strip().replace(",", "")
    if is_check(greet):
        print("$0")
    elif greet[0] == "h" and not is_check(greet):
        print("$20")
    else:
        print("$100")


def is_check(word):
    word = word.split()

    return word[0] == "hello"


main()
