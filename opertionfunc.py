num1 = int(input("enter first number: "))
print(num1)
num2 = int(input("enter second number: "))
print(num2)
print("These are the operators you can use :")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Module")
result = 0
operator = input("Please choose an option from these (1,2,3,4,5):")
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
    print(result)
def mul(num1,num2):
    return num1*num2
    print(result)
def div(num1,num2):
    return num1//num2
    print(result)
def mod(num1,num2):
    return num1%num2
    print(result)
if operator=="1":
    result=add(num1,num2)
    print(result)
if operator=="2":
    result=sub(num1,num2)
    print(result)
if operator=="3":
    result=mul(num1,num2)
    print(result)
if operator=="4":
    result=div(num1,num2)
    print(result)
if operator=="5":
    result=mod(num1,num2)
    print(result)
