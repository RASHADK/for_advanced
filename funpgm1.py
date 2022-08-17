def max_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
sum=max_of_three(1,2,3)
print(sum)
def max_of_three(a,b,c):
    sum=(a,b,c)
    return sum
num1=int(input("Enter a number:"))
sum=max_of_three(num1,2,3)
print(sum)
