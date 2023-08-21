
def data() :
    user_name = input("Enter your name :")
    age = int(input("Enter your age :"))
    dob = input("Enter your date of birth (YYYY_MM_DD):")
    with open("data.txt","w") as file:
        file.write(f"User NAME:{user_name}/n")
        file.write(f"Age:{age}/n")
        file.write("Date of Birth:{dob}/n")
        print(f"User information saved to data.txt")
data()






