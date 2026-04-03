sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

# Counting occurrences
for word in words:
    word = word.lower()  # to make counting case-insensitive
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")
for key, value in frequency.items():
    print(key, ":", value)