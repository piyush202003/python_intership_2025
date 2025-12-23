while(1):
    print("Enter your Information as below")
    name = input("Enter your Name: ")
    age = input("Enter your Age: ")
    city = input("Enter your City Name: ")
    print(f"My name is {name}, I am {age} years old, and I live in {city.upper()}. ")
    i = input("If want to continue press 1 else to stop press 0 and enter= ")
    if i=='0':
        print("Program is ended")
        break


# Enter your Information as below
# Enter your Name: Ram
# Enter your Age: 18
# Enter your City Name: nashik
# My name is Ram, I am 18 years old, and I live in NASHIK. 
# If want to continue press 1 else to stop press 0 and enter= 0
# Program is ended