sym = [" ", ".", "?", "!", ",", ":", ";", "(", ")", "[", "]", "'", '"', "-", "_", "/", "\\", "@", "#", "$", "*", "&", "%", "<", ">"]
def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    validated = ""
    numcheck = 0

    if len(s) >= 2 and len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            for ch in s:
                if ch not in sym:
                    if ch.isnumeric() and numcheck == 0 and ch != "0":
                        numcheck += 1
                        validated += ch
                    elif ch.isnumeric() and numcheck > 0:
                        numcheck += 1
                        validated += ch
                    elif ch.isalpha() and numcheck == 0:
                        validated += ch
    if validated == s:
        return True
    else:
        return False

main()