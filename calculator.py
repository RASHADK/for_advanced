replace = ""
flag = "print"
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
    replace1 = "Addition"
    result = a + b
if operator == "2":
    if a < b:
        flag = "Do not print"
        print("Cannot subtract the first number is less than the second number")
    else:
        replace1 = "Subtraction"
        result = a - b
if operator == "3":
    replace1 = "Multiplication"
    result = a * b
if operator == "4":
    replace1 = "Division"
    result = a / b
if operator == "5":
    replace1 = "Modulus"
    result = a % b
if flag == "print":
    print("The result of ", replace1, "of", a, "and", b, "is", result)
