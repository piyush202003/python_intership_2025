print("Please enter 5 numbers: ")
let=[]
for i in range(5):
    let.append(int(input(f"Enter number {i+1} :")))

print("List of numbers: ", let)
print("Sum=",sum(let))
print("Average= ", sum(let)/5)
print("Largest Number= ",max(let))


# Please enter 5 numbers: 
# Enter number 1:1
# Enter number 2:2
# Enter number 3:3
# Enter number 4:4
# Enter number 5:5
# List of numbers:  [1, 2, 3, 4, 5]
# Sum= 15
# Average=  3.0
# Largest Number=  5
