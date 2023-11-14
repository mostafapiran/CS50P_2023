x = ["42", "forty-two", "forty two"]
y = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

if y in x:
    print("Yes")
else:
    print("No")