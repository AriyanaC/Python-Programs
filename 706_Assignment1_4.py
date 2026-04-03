import sys

# ----------- Part 1: Variable Creation -----------

print("----- Part 1: Variable Creation -----")

a = 12                      # Integer
b = 3.44                    # Float
c = 1 + 5j                  # Complex
d = True                    # Boolean
e = "Python Programming is fun"    # String

variables = [a, b, c, d, e]

for var in variables:
    print("Value:", var)
    print("Type:", type(var))
    print()


# ----------- Part 2: Memory Size -----------

print("----- Part 2: Memory Size -----")

for var in variables:
    print("Value:", var)
    print("Size (in bytes):", sys.getsizeof(var))
    print()


# ----------- Part 3: Complex Numbers -----------

print("----- Part 3: Complex Number Operations -----")

z = c
print("Complex Number:", z)
print("Real Part:", z.real)
print("Imaginary Part:", z.imag)
print("Magnitude:", abs(z))


# ----------- Part 4: Boolean Operations -----------

print("\n----- Part 4: Boolean Operations -----")

x = True
y = False

print("x AND y:", x and y)
print("x OR y:", x or y)
print("NOT x:", not x)


# ----------- Part 5: Type Conversion -----------

print("\n----- Part 5: Type Conversion -----")

num = 10
flt = 5.75
str_num = "20"
bool_val = True

# Conversions
print("Integer to Float:", float(num))
print("Float to Integer:", int(flt))
print("Integer to String:", str(num))
print("String to Integer:", int(str_num))
print("Boolean to Integer:", int(bool_val))
print("Integer to Complex:", complex(num))