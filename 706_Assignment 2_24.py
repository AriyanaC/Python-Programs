def top_k_frequency(l1, k):
    frequency = {}

    #Count Frequency
    for i in l1:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    #Sort based on frequency(descending)
    sorted_items = sorted(frequency.items(), key = lambda x: x[1], reverse = True)

    return sorted_items[:k]

l1 = eval(input("Enter a list of numbers:"))

k = int(input("Enter value of k:"))

result = top_k_frequency(l1, k)

print("Top", k, "frequent elements:")
for num, freq in result:
    print(num, ":", freq)