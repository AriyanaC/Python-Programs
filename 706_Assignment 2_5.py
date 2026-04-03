t1 = eval(input("Enter a tuple of numbers:"))
count = 0

for i in t1:
    if i % 2 == 0:
        count += 1

print("Number of even numbers:", count)