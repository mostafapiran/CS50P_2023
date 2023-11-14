price = 50
gain = 0

while gain < price:
    print(f"Amount Due: {price - gain}")
    x = int(input("Next coin: ").strip())
    if x == 25 or x == 10 or x == 5:
        gain += x
    else:
        continue

print(f"Change Owed: {gain - price}")