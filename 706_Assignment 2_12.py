set1 = eval(input("Enter a set:"))
set2 = eval(input("Enter another set:"))

union_result = set1.union(set2)
intersection_result = set1.intersection(set2)
difference_result = set1.difference(set2)

print("\nUnion:", union_result)
print("Intersection:", intersection_result)
print("Difference (Set1 - Set2):", difference_result)