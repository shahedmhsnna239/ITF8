def triangle():
    base = int(input("enter a base"))
    rid1 = int(input("enter a rib 1"))
    rid2 = int(input("enter a rib 2"))
    rise = int(input("enter a rise"))
    area = 0.5 * base * rise
    per = base + rid1 + rid2
    print(area , per)

    if area >= 10:
        print("large")
    elif area < 10:
        print("small")
    elif area <=0:
        print("invaildinput")
triangle()


def square():
    rid = int(input("enter a rid"))
    area = rid * rid
    per = rid + rid + rid + rid
    print(area , per)
    if area >= 10:
        print("large")
    elif area < 10:
        print("small")
    elif area <= 0:
        print("invaildinput")

square()

def circle():
    radius = int(input("enter a radius"))
    area = radius * radius * 3.14
    per = 2 * radius * 3.14
    print(area , per)
    if area >= 10:
        print("large")
    elif area < 10:
        print("small")
    elif area <= 0:
        print("invaildinput")


circle()
