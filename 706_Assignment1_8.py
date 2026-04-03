# Function to check triangle validity
def is_valid_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

# Function to classify triangle
def classify_triangle(a, b, c):
    if a == b == c:
        return "Equilateral Triangle"
    elif a == b or b == c or a == c:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"


# Main program
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if is_valid_triangle(a, b, c):
    print("\nValid Triangle")
    print("Type:", classify_triangle(a, b, c))
else:
    print("\nNot a valid triangle")

