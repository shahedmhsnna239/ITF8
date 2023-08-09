def menu():
    while True:
        selection = int(input("1 . Sum/n"
                              "2 . Subtract/n"
                              "3 . Multiply/n"
                              "4 . Division/n"
                              "5 . Calculate triangle area/n"
                              "6 . Calculate circle area/n"
                              "7 . Calculate rectangle area/n"
                              "8 . Exit"))
        if selection in ["1" , "2" , "3" , "4", "5"]:
            num1 =float(input("enter num 1"))
            num2 =float(input("enter num 2"))
            if selection =="1":


        elif selection == 2 :
            base = float(input("base"))
            rise = float(input("rise"))
            area = 0.5 * base * rise
            print(("area")
        elif selection == 3:
            rid = float(input("rid"))
            area = rid * rid
            print("area")

