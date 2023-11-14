x = input("Greeting: ").strip().lower()

if x.startswith("hello"):
    i = 0
elif x.startswith("h"):
    i = 20
else:
    i = 100

print(f"${i}")

#hi