
def total_calculation(sub:list[int]):
    total=0
    for i in range(5):
        total+=sub[i]
    return total

def percentage_calculation(sub: list[int]):
    return (total_calculation(sub)/500)*100

def grade_assignment(per:float):
    if per >= 75:
        print("Distinction")
    elif per >= 60 and per <= 74:
        print("Frist Class")
    elif per >=50 and per <= 59:
        print("Second Class")
    else: 
        print("Fail")


print("Enter Students Informations: ")
name = input("Enter Name: ")
print("Enter subjects marks out of 100 ")
sub=[]
for i in range(5):
    sub.append(int(input(f"Enter subject {i+1} marks: ")))
print("---------- Now results are ----------")
print("Total marks: ",total_calculation(sub))
per=percentage_calculation(sub)
print("Percentage: ", per)
grade_assignment(per)


# Enter Students Informations: 
# Enter Name: Ram
# Enter subjects marks out of 100 
# Enter subject 1 marks: 40
# Enter subject 2 marks: 30
# Enter subject 3 marks: 56
# Enter subject 4 marks: 43
# Enter subject 5 marks: 66
# ---------- Now results are ----------
# Total marks:  235
# Percentage:  47.0
# Fail