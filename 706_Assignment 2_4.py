s1 = input("Enter a string:")
count = 0

for i in s1:
    if i in "AEIOUaeiou":
        count += 1

print("Number of vowels:", count)