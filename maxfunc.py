def max_of_three(a,b,c):
   if a>b and a>c:
        return a
   elif b>a and b>c:
        return b
   else:
        return c
# num1=int(input("enter a number1:"))
# num2=int(input("enter a number2:"))
# num3=int(input("enter a number3:"))
sum=max_of_three(22,33,44)
print(sum)