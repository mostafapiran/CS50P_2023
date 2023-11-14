import re


def main():
    print(count(input("Text: ")))


def count(s):
    regex = "(^|\W)um($|\W)"
    match = re.findall(regex, s, re.IGNORECASE)
    if match:
        return(len(match))


if __name__ == "__main__":
    main()