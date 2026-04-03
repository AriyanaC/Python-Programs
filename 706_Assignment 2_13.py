data = {}

n = int(input("Enter number of elements: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

print("\nDictionary contents:")
for key, value in data.items():
    print(key, ":", value)