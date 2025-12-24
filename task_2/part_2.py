
def validate(password: str):
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXVZ"
    lowercase="abcdefghijklmnopqrstuvwxyz"
    digit="0123456789"
    special="@#$%&"
    u=0
    l=0
    d=0
    s=0
    for i in password:
        if u==0 and i in uppercase:
            u+=1
        elif l==0 and i in lowercase:
            l+=1
        elif d==0 and i in digit:
            d+=1
        elif s==0 and i in special:
            s+=1
    if u!=0 and l!=0 and d!=0 and s!=0:
        return print("Valid Password")
    else:
        print("Invalid Password")
        if u==0:
            print("Don't have any UpperCase")
        if l==0:
            print("Don't have any LowerCase")
        if d==0:
            print("Don't have any digits")
        if s==0:
            print("Don't have any special charecters")
    return


print("Rules for entering the password")
print("Rule 1: At least 1 uppercase letter")
print("Rule 2: At least 1 lowercase letter")
print("Rule 3: At least 1 digit")
print("Rule 4: At least 1 special Character(@ # $ % &)")

password = input("Enter your password: ")

validate(password)

# Rules for entering the password
# Rule 1: At least 1 uppercase letter
# Rule 2: At least 1 lowercase letter
# Rule 3: At least 1 digit
# Rule 4: At least 1 special Character(@ # $ % &)
# Enter your password: password
# Invalid Password
# Don't have any UpperCase
# Don't have any digits
# Don't have any special charecters

# Rules for entering the password
# Rule 1: At least 1 uppercase letter
# Rule 2: At least 1 lowercase letter
# Rule 3: At least 1 digit
# Rule 4: At least 1 special Character(@ # $ % &)
# Enter your password: Password@123
# Valid Password