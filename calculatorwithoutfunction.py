replace = ""
print("********** welcome to the calculator*********")
a = int(input("enter first number: "))
print(a)
b = int(input("enter second number: "))
print(b)
print("These are the operators you can use :")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Module")
result = 0
operator = input("Please choose an option from these (1,2,3,4,5):")
if operator == "1":
    result = a + b
    print("The result of ",a,"and",b,"is",result)
if operator == "2":
    if a < b:
        print("Cannot subtract the first number is less than the second number")
    else:
        result = a - b
        print("The result of Subtraction of ",a,"and",b,"is",result)
if operator == "3":
    if a==0 or b==0:
        print("cannot multiply by zero")
    else:
        result=a*b
        print("The result of Multiplication of ",a,"and",b,"is",result)
if operator == "4":
    if b==0:
        print("cannot divide by zero")
    else:
        result=a//b
        print("The result of division of",a,"and",b,"is",result)
if operator == "5":
    if b==0:
        print("cannot modulus")
    else:
        result = a % b
        print("The result of", a, "and", b, "is", result)
