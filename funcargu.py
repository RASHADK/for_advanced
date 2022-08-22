# def reusable(num):
#     for i in range(1,num):
#         print("This is reusable func 1")
#         print("This is reusable func 2")
#         print("This is reusable func 3")
#         print("This is reusable func 4")
#         print("----------------------------")
# reusable(10)
def reusable():
        print("This is reusable func 1")
        print("This is reusable func 2")
        print("This is reusable func 3")
        print("This is reusable func 4")
        print("----------------------------")

num=int(input("enter a number:"))
for i in range(1,num):
     reusable()