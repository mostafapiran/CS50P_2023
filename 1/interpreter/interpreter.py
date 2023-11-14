x, c, y = input("Enter an expression: ").strip().split(" ")

if c == "+":
    ans = float(x) + float(y)
elif c == "-":
    ans = float(x) - float(y)
elif c == "*":
    ans = float(x) * float(y)
elif c == "/":
    ans = float(x) / float(y)

print(F"{ans:.1f}")