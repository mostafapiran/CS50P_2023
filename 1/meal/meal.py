def main():

    sch = [
        {"meal" : "breakfast time", "start hour" : 7, "end hour" : 8},
        {"meal" : "lunch time", "start hour" : 12, "end hour" : 13},
        {"meal" : "dinner time", "start hour" : 18, "end hour" : 19}
    ]

    time = input("What time is it? ").strip()
    time = float(convert(time))

    for x in sch:
        if time >= float(x["start hour"]) and time <= float(x["end hour"]):
            print(x["meal"])


def convert(time):

    c = 0
    if time.rfind(" a.m.") != -1:
        time = time.replace(" a.m.", "")
    elif time.rfind(" p.m.") != -1:
        time = time.replace(" p.m.", "")
        c = 12

    h, m = time.split(":")
    t = float(h) + c + (float(m) / 60)
    return t

if __name__ == "__main__":
    main()