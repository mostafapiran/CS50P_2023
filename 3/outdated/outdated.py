def main():

    moon = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    while True:
        date = input("Date: ")
        try:
            if "/" in date:
                mm, dd, yyyy = date.split("/")
            elif "," in date:
                mmdd, yyyy = date.split(", ")
                mm, dd = mmdd.split(" ")
                mm = (moon.index(mm)) + 1
            if int(mm) > 12 or int(dd) > 31:
                raise ValueError
        except (AttributeError, ValueError, NameError, KeyError):
            pass
        else:
            print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
            break


if __name__ == "__main__":
    main()