# Function to generate all subsets using bit masking
def generate_subsets(s):
    n = len(s)
    subsets = []

    # Loop from 0 to 2^n - 1
    for i in range(2 ** n):
        subset = []

        for j in range(n):
            # Check if j-th bit is set
            if (i >> j) & 1:
                subset.append(s[j])

        subsets.append(subset)

    return subsets


# Main program
def main():
    # Input
    elements = list(map(int, input("Enter elements (space-separated): ").split()))

    # Generate subsets
    result = generate_subsets(elements)

    print("\nAll Possible Subsets:")
    for subset in result:
        print(subset)


# Run
main()