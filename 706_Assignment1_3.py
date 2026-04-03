import math

print("----- MENU -----")
print("Area Calculations")
print("1 → Area of Circle")
print("2 → Area of Rectangle")
print("3 → Area of Triangle")
print("4 → Area of Square")
print("5 → Area of Parallelogram")
    
print("\nVolume Calculations")
print("6 → Volume of Cube")
print("7 → Volume of Cuboid")
print("8 → Volume of Sphere")
print("9 → Volume of Cylinder")
print("10 → Volume of Cone")
print("\n0 → Exit")

while True:
    choice = int(input("\nEnter your choice (0-10): "))

    if choice == 0:
        print("Exiting program. Thank you!")
        break
    match choice:

        # -------- AREA --------
        case 1:
            r = float(input("Enter radius: "))
            area = math.pi * r * r
            print("Area of Circle =", area)

        case 2:
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            print("Area of Rectangle =", l * b)

        case 3:
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            print("Area of Triangle =", 0.5 * b * h)

        case 4:
            s = float(input("Enter side: "))
            print("Area of Square =", s * s)

        case 5:
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            print("Area of Parallelogram =", b * h)

        # -------- VOLUME --------
        case 6:
            s = float(input("Enter side: "))
            print("Volume of Cube =", s ** 3)

        case 7:
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            h = float(input("Enter height: "))
            print("Volume of Cuboid =", l * b * h)

        case 8:
            r = float(input("Enter radius: "))
            volume = (4/3) * math.pi * r ** 3
            print("Volume of Sphere =", volume)

        case 9:
            r = float(input("Enter radius: "))
            h = float(input("Enter height: "))
            volume = math.pi * r ** 2 * h
            print("Volume of Cylinder =", volume)

        case 10:
            r = float(input("Enter radius: "))
            h = float(input("Enter height: "))
            volume = (1/3) * math.pi * r ** 2 * h
            print("Volume of Cone =", volume)

        case _:
            print("Invalid choice! Please select between 0 and 10.")