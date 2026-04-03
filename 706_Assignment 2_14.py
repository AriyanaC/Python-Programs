data = {}

n = int(input("Enter number of key-value pairs: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

# Swapping keys and values
swapped = {}

for key, value in data.items():
    swapped[value] = key

# Display results
print("\nOriginal Dictionary:", data)
print("Swapped Dictionary:", swapped)