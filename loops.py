# num_of_student = int(input("Enter num_of_student:"))
def student():
    num_of_student = int(input("Enter num_of_student:"))
    for i in range (1 , num_of_student+1):
        marks_count = int(input(f"Enter marks_count for student {i}"))
        my_mark = []
        for mark_num in range(0, marks_count):
            mark = float(input(f"Enter mark {mark_num+1} for student{i} : "))
            my_mark.append(mark)
        averege = sum(my_mark) / marks_count
        print(my_mark)
        print(averege)
        print(max(my_mark))
        print(min(my_mark))
student()

