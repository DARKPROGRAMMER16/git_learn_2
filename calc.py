a,b = input("enter two digits comma seprated : ").split(",")
a=int(a)
b=int(b)
operator = input("enter the operator : \n add : + \n subtract : - \n multiply : * \n div : / \n ")
if operator=='+':
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="/":
    print(a/b)
else:
    print("error")
