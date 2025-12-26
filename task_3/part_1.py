class Students:
     def __init__(self):
         self.mem={}
         
     def calculate_total(self, sub) :
         return sum(sub)
         
     def calculate_percentage(self, sub) :
         return (sum(sub)/500)*100
         
     def assign_grade(self, percent) :
         if percent>=75:
             return "Distinction"
         elif percent>=60 and percent<=74:
             return "First Class"
         elif percent>=50 and percent<=59:
             return "Second Class"
         return "Fail"
         
     def display_details(self, std) :
         if std not in self.mem:
             return print("Student. with this ID is not present")
         print("Printing the information of students")
         print(f"Name={self.mem[std]["name"]}")
         print("Marksheet=")
         for i in range(5):
             print(f"Subject{i+1} = {self.mem[std]["sub"][i]}")
         print("Total marks=", self.mem[std]["total"]) 
         print("Percentage= ",self.mem[std]["percent"])
         print("Obtained Grade= ", self.mem[std]["grade"])
             
             
     def std_add(self, std_id, name, sub):
         total= self.calculate_total(sub)
         percent= self.calculate_percentage(sub)
         grade= self.assign_grade(percent)
         
         self.mem[std_id]= {
             "name": name,
             "sub" : sub,
             "total": total,
             "percent": percent,
             "grade": grade
         }
             
             
obj = Students()             
std_id=0
while(True):
    print("Menu:")
    print ("1: Add students")
    print ("2: Display Student info")
    print ("3: Exit")
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        std_id+=1
        print(" Enter Student info")
        name=input("Enter student name= ")
        sub=[]
        print("Enter marks of subjects =")
        for i in range(5):
            sub.append(int(input(f"Subject{i+1} = ")))
        obj.std_add(std_id, name.upper(), sub)    
        print("Student info is added")
    elif ch == 2:
        std= int(input("Enter student id= "))    
        obj.display_details(std)
    else: 
        print(" Program is stopped ")
        break
          