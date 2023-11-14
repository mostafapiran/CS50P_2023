x = input("camelCase: ").strip()

snake = ""

for i in x:
    if i.isupper():
        snake += "_"
        snake += i.lower()
    else:
        snake += i

print(f"snake_case: {snake}")