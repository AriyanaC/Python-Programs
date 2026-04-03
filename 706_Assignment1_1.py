def add(a,b):             #Addition function
    return a + b
    
def subtract(a,b):         #Subtraction function
    return a - b
    
def multiply(a,b):         #Multiplication function
    return a * b
    
def divide(a,b):           #Division function
    if b == 0:
        return "Oops, Division by Zero is not allowed"
    return a / b
    
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


print("\nResults:")
print("Addition:", add(num1,num2))
print("Subtraction:", subtract(num1,num2))
print("Multiplication:", multiply(num1,num2))
print("Division:", divide(num1,num2))