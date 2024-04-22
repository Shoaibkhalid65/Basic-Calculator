first=int(input("enter first number:"))
operator=input("enter operator from following:\n'+,-,*,/,//,%,**'")
second=int(input("enter second number:"))
if operator=="+":
    print(f"the addition of {first} and {second} is {first+second}")
elif operator=="-":
    print(f"the subtraction of {first} and {second} is {first-second}")
elif operator=="*":
    print(f"the multiplication of {first} and {second} is {first*second}")
elif operator=="/":
    print(f"the division of {first} and {second} is {first/second}")
elif operator=="%":
    print(f"the modulus of {first} and {second} is {first%second}")
elif operator=="//":
    print(f"the floor division of {first} and {second} is {first//second}")
elif operator=="**":
    print(f"the power of {first} and {second} is {first**second}")


