list=[1,2,3,4,5,6,7,8,9,10]
def add(list):
    sum=0
    for i in list:
        sum=sum+i
    return sum
def sum(list):
    sum=1
    for i in list:
       sum=sum*i
    return sum
def square(list):
    sum=[]
    for i in list:

        sum.append(i*i)
    return sum
print(sum(list))
print(square(list))
print(add(list))
