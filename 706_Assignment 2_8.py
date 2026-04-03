l1 = eval(input("Enter a list of numbers:"))

unique_list = []

for i in l1:
    if i not in unique_list:
        unique_list.append(i)

print("List after removing duplicates:", unique_list)