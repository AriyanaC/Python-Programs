# Function to group anagrams
def group_anagrams(words):
    anagram_dict = {}

    for word in words:
        # Sort the word to create a key
        key = ''.join(sorted(word))

        if key in anagram_dict:
            anagram_dict[key].append(word)
        else:
            anagram_dict[key] = [word]

    return list(anagram_dict.values())


# Main program
words = input("Enter words (space-separated): ").split()

result = group_anagrams(words)

print("\nGrouped Anagrams:")
for group in result:
    print(group)