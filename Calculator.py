def add(x,y):
    return int(x+y)

def substract(x,y):
    return int(x-y)

def multiply (x,y):
    return int(x*y)

def division (x,y):
    return x/y

a=input("Welcome to this simple calculator, Whats your name?")
print(f"Hello {a}, glad to see you here!!")

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
b=int(input(f"{a}, please select an operation (1/2/3/4)"))

x=float(input("Alright!! Enter first number: "))
y=float(input("Nice!! Enter second number: "))

match b:
    case 1:
        print(add(x,y))
    
    case 2:
        print(substract(x,y))

    case 3:
        print(multiply (x,y))

    case 4:
        print(division (x,y))
