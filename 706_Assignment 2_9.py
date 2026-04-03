l1 = eval(input("Enter a list of numbers:"))
reversed_list = []

length = len(l1)

for i in range(length - 1, -1, -1):
    reversed_list.append(l1[i])

print("Reversed List:", reversed_list)