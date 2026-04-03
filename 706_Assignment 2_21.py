l1 = eval(input("Enter a list:"))

target = int(input("Enter target:"))

for i in range(len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] + l1[j] == target:
            print("Indices:", (i,j))
            print("Numbers:", l1[i], "+", l1[j], "=", target)