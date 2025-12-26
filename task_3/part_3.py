import csv
class Parent:
    def __init__(self):
        self.mem={}
        with open("Emp_Data.csv", 'w', newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(["Emp_Id","Name","Salary","HRA","DA","Total."])
    
    def calculate_hra(self, salary):
        return 0.2 * salary
        
    def calculate_da(self, salary):
        return 0.1 * salary
        
    def calculate_total_salary(self, hra, da, salary):
        return hra + da + salary
    
    def add_emp(self, emp_id, emp_name, emp_salary):
        hra = self.calculate_hra(emp_salary)
        da = self.calculate_da(emp_salary)
        total = self.calculate_total_salary(hra, da, emp_salary)
        with open("Emp_Data.csv", 'w', newline='') as emp_data:
            csvwriter = csv.writer(emp_data)
            csvwriter.writerow([emp_id, emp_name, emp_salary, hra, da, total])
        print("Employee info is saved with id: ", emp_id)
    
class Child(Parent):
    def display_salary_slip(self, emp_id):
        data=[]
        with open('Emp_Data.csv', mode='r') as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                if line[0]==str(emp_id):
                    data=line
                    break
        if not data:
            print("There is no employee with Id: ", emp_id)
            return
        print("Printing the salary slip of employee with id ", emp_id)
        print("Name: ", data[1])
        print("Salary: ", float(data[2]))
        print("HRA: ", float(data[3]))
        print("DA: ", float(data[4]))
        print("Total: ", float(data[5]))
        print("----------------------")

emp_id=0
obj = Child()
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
            obj.add_emp(emp_id, emp_name, emp_salary)
            
    elif ch == 2:
        emp_id = int(input("Enter employee id="))
        obj.display_salary_slip(emp_id)
        
    elif ch == 3:
        print("Program is stopped")
        break
    else:
        print("Wrong input is given")