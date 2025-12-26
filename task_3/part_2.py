
class Parent:
    def __init__(self):
        self.mem={}
    
    def calculate_hra(self, salary):
        return 0.2 * salary
        
    def calculate_da(self, salary):
        return 0.1 * salary
        
    def calculate_total_salary(self, hra, da, salary):
        return hra + da + salary
    
    def add_emp(self, emp_id, emp_name, emp_salary):
        self.mem[emp_id]={
            "name":emp_name.upper(),
            "salary":emp_salary
        }
        
        hra = self.calculate_hra(emp_salary)
        da = self.calculate_da(emp_salary)
        total = self.calculate_total_salary(hra, da, emp_salary)
        
        self.mem[emp_id]['hra']=hra
        self.mem[emp_id]['da']=da
        self.mem[emp_id]['total']=total
        print("Employee info is saved with id: ", emp_id)
    
class Child(Parent):
    
    def add_emp(self, emp_id, emp_name, emp_salary):
        super().add_emp(emp_id, emp_name, emp_salary)
    
    def display_salary_slip(self, emp_id):
        if emp_id not in self.mem:
            print("There is no employee with Id: ", emp_id)
            return
        print("Printing the salary slip of employee with id ", emp_id)
        print("Name: ", self.mem[emp_id]['name'])
        print("Salary: ", self.mem[emp_id]['salary'])
        print("HRA: ", self.mem[emp_id]['hra'])
        print("DA: ", self.mem[emp_id]['da'])
        print("Total: ", self.mem[emp_id]['total'])
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