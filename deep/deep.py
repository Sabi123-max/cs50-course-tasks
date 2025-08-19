word = input("what is the answer to the Great Question of Life, the Universe and Everything? ").lower().replace("-","").replace(" ","")

if word == "42" or word == "fortytwo":
    print("Yes")
else:
    print("No")

