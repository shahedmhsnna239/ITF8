def triangle():
    x = int(input("enter a base"))
    y = int(input("enter a rib 1"))
    z = int(input("enter a rib 2"))
    a = int(input("enter a rise"))
    area = 0.5 * x * a
    per = x + y + z
    print(area , per)
triangle()

def square():
    x = int(input("enter a rid"))
    area = x * x
    per = x + x + x + x
    print(area , per)
square()