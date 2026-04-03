# Function to find longest substring without repeating characters
def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    longest_substring = ""

    for right in range(len(s)):
        # If duplicate found, shrink window
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        # Update max length and substring
        if right - left + 1 > max_length:
            max_length = right - left + 1
            longest_substring = s[left:right+1]

    return longest_substring, max_length


string = input("Enter a string: ")

substring, length = longest_unique_substring(string)

print("Longest substring without repeating characters:", substring)
print("Length:", length)