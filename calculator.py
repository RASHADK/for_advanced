print("********** welcome to the calculator*********")
a=int(input("enter first number: "))
print(a)
b=int(input("enter second number: "))
print(b)
print("These are the operators you can use :")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Module")
operator=input("Please choose an option from these (1,2,3,4,5):")
if operator=="1":
    print("This is an Addition Operation")
    print("The sum of the two numbers is :",a+b)
if operator=="2":
    print("This is a Subtraction Operation")
    print("The difference of the two numbers:",a-b)
if operator=="3":
    print("This is a Multiplication Operation")
    print("The product of two numbers is:",a*b)
if operator=="4":
    print("This is a division Operator")
    print("The division of two numbers is:",a/b)
if operator=="5":
    print("This is a Modulus Operator")
    print("The modulus of two number is:",a%b)


