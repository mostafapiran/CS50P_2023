vowel = ["a", "o", "u", "i", "e"]

input = input("Input: ").strip()
out = ""

for i in input:
    if i.lower() not in vowel:
        out += i

print(f"Output: {out}")