def calculate (mark1, hour1, mark2, hour2, mark3, hour3):
    total = (mark1 * hour1) + (mark2 * hour2) + (mark3 * hour3)
    averge =total /(hour1+ hour2+hour3)
    return averge

mark1 = 99
hour1 = 1
mark2 = 95
hour2 = 3
mark3 = 91
hour3 = 2
mark4 = 90
hour4 = 3
mark5 = 80
hour5 = 2
mark6 = 85
hour6 = 2


averge1 = calculate(mark1,hour1,mark2,hour2,mark3,hour3)
print(averge1)
averge2 = calculate(mark4,hour4,mark5,hour5,mark6,hour6)
print(averge2)
cumulative = ((averge1 * (hour1 + hour2 + hour3))+(averge2 * (hour4 + hour5 + hour6)))/(hour1 + hour2 + hour3 + hour4 + hour5 + hour6)
print(cumulative)




