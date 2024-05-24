def generate_permutations(n):
    def backtrack(start=0):
        # Base case: if all elements are placed, print the permutation
        if start == n:
            print(permutation)
            return

        # Try placing each number at the current position
        for i in range(start, n):
            # Swap the elements at positions start and i
            permutation[start], permutation[i] = permutation[i], permutation[start]

            # Recursively generate permutations for the remaining elements
            backtrack(start + 1)

            # Undo the swap for backtracking
            permutation[start], permutation[i] = permutation[i], permutation[start]

    # Initialize the permutation array
    permutation = list(range(1, n + 1))

    # Start the recursive process
    backtrack()

# Example usage for n = 3
generate_permutations(3)


