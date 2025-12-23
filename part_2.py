s="My name is Piyush, I am 22 years old, and I live in MALKAPUR."
s=input("Enter the sentence for evaluation: ")
s=s.lower()
d={}
for i in s:
    if i>="a" and i<="z":
        if i in d:
            d[i]+=1
        else:
            d[i]=1

print(d)


# Enter the sentence for evaluation: This is the test drive for python.
# {'t': 5, 'h': 3, 'i': 3, 's': 3, 'e': 3, 'd': 1, 'r': 2, 'v': 1, 'f': 1, 'o': 2, 'p': 1, 'y': 1, 'n': 1}
