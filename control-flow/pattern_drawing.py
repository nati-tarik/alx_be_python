# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer loop (while) to handle rows
while row < size:
    # Inner loop (for) to handle columns
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
