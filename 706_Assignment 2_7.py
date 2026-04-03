l1 = eval(input("Enter a list of numbers:"))

l2 = [i for i in l1 if i % 2 == 0]

print("New list of even numbers:", l2)