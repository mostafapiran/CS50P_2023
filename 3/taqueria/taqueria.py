def main():
    f = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    pr = 0

    while True:
        try:
            item = input("Item: ").title().strip()
            pr = pr + f[item]
            print(f"Total: ${pr:.2f}")
        except EOFError:
            print()
            break
        except KeyError:
            pass

if __name__ == "__main__":
    main()
