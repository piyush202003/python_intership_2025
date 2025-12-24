
def add_emp(emp_dict:dict, emp_id: int):
    emp_dict[emp_id]={
            "name":emp_name.upper(),
            "salary":emp_salary
        }
    for i in emp_dict:
        salary=emp_dict[i]['salary']
        hra = 0.2 * salary
        da = 0.1 * salary
        total = hra + da + salary
        emp_dict[i]['hra']=hra
        emp_dict[i]['da']=da
        emp_dict[i]['total']=total
    print("Employee info is saved")
    return emp_dict

emp_id=0
emp_dict={}

while(True):
    print("1: Add the employee")
    print("2: Print the Slip")
    print("3: Exit")
    ch = int(input("Enter your choise: "))
    if ch ==1:
        n = int(input("No. of employee you want to add= "))
        for i in range(n):
            print(f"{i+1} Employee Info ")
            emp_id+=1
            emp_name=input("Enter employee name= ")
            emp_salary=float(input("Enter employee salary= "))
            emp_dict = add_emp(emp_dict, emp_id)
    elif ch == 2:
        print("Printing the salary slip of All employees")
        for i in emp_dict:
            print("Employ id: ",i)
            print("Name: ", emp_dict[i]['name'])
            print("Salary: ", emp_dict[i]['salary'])
            print("HRA: ", emp_dict[i]['hra'])
            print("DA: ", emp_dict[i]['da'])
            print("Total: ", emp_dict[i]['total'])
            print("----------------------")
    elif ch == 3:
        print("Program is stopped")
        break
    else:
        print("Wrong input is given")

# 1: Add the employee
# 2: Print the Slip
# 3: Exit
# Enter your choise: 1
# No. of employee you want to add= 2
# 1 Employee Info 
# Enter employee name= ram
# Enter employee salary= 6000
# Employee info is saved
# 2 Employee Info 
# Enter employee name= sham
# Enter employee salary= 5000
# Employee info is saved
# 1: Add the employee
# 2: Print the Slip
# 3: Exit
# Enter your choise: 5
# Wrong input is given
# 1: Add the employee
# 2: Print the Slip
# 3: Exit
# Enter your choise: 2
# Printing the salary slip of All employees
# Employ id:  1
# Name:  RAM
# Salary:  6000.0
# HRA:  1200.0
# DA:  600.0
# Total:  7800.0
# ----------------------
# Employ id:  2
# Name:  SHAM
# Salary:  5000.0
# HRA:  1000.0
# DA:  500.0
# Total:  6500.0
# ----------------------
# 1: Add the employee
# 2: Print the Slip
# 3: Exit
# Enter your choise: 3
# Program is stopped