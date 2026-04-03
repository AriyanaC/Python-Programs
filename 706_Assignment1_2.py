# ----------- FUNCTIONS -----------

# Basic operations
def union_sets(a, b):
    return a.union(b)

def intersection_sets(a, b):
    return a.intersection(b)

def difference_sets(a, b):
    return a.difference(b)

def symmetric_difference_sets(a, b):
    return a.symmetric_difference(b)


# Subset and Superset
def check_subset_superset(a, b):
    print("Is Set1 a subset of Set2?:", a.issubset(b))
    print("Is Set1 a superset of Set2?:", a.issuperset(b))


# Element check
def check_element(s, element):
    if element in s:
        print("Element is present in the set.")
    else:
        print("Element is NOT present in the set.")


# Count elements
def count_elements(s):
    return len(s)


# List to set (remove duplicates)
def list_to_set(lst):
    return set(lst)


# Power set
def power_set(s):
    s = list(s)
    n = len(s)
    result = []

    for i in range(1 << n):
        subset = [s[j] for j in range(n) if (i & (1 << j))]
        result.append(subset)
    return result


# ----------- MAIN PROGRAM -----------
 # INPUT (simple and correct)
set1 = set(map(int, input("Enter elements of Set 1 (space-separated): ").split()))
set2 = set(map(int, input("Enter elements of Set 2 (space-separated): ").split()))

# BASIC OPERATIONS
print("\n--- Basic Set Operations ---")
print("Union:", union_sets(set1, set2))
print("Intersection:", intersection_sets(set1, set2))
print("Difference (Set1 - Set2):", difference_sets(set1, set2))
print("Symmetric Difference:", symmetric_difference_sets(set1, set2))

# SUBSET / SUPERSET
print("\n--- Subset & Superset ---")
check_subset_superset(set1, set2)

# ELEMENT CHECK
element = int(input("\nEnter element to check in Set1: "))
check_element(set1, element)

# COUNT
print("\nNumber of elements in Set1:", count_elements(set1))
print("\nNumber of elements in Set2:", count_elements(set2))
# LIST TO SET
lst = list(map(int, input("\nEnter list elements (space-separated): ").split()))
print("Set after removing duplicates:", list_to_set(lst))

# POWER SET
print("\n--- Power Set of Set1 ---")
pset = power_set(set1)
for subset in pset:
    print(subset)
