#Learning user defined functions


def add(a,b):
    return a+b
def diff(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("--------Calculations--------")
print("The sum of",a,"and",b,"is",add(a,b))
print("The difference of",a,"and",b,"is",diff(a,b))
print("The multiplication of",a,"and",b,"is",mul(a,b))
print("The division of",a,"by",b,"is",div(a,b))
