l1 = eval(input("Enter a list of numbers:"))

frequency = {}

for num in l1:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency of elements:")
for key, value in frequency.items():
    print(key, ":", value)