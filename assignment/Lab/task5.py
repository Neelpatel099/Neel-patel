











#13.Practical Example 1: Write a Python program to print each fruit in a list using a simple for loop. List1 = ['apple', 'banana', 'mango']

fruits = ['apple', 'banana', 'mango']

# Basic loop
for fruit in fruits:
    print(fruit)

print()  # Empty line for separation

# Loop with index
for index, fruit in enumerate(fruits):
    print(f"Item {index}: {fruit}")

print()

# Loop with condition
for fruit in fruits:
    if fruit.startswith('m'):
        print(f"Starts with 'm': {fruit}")

#14.Practical Example 2: Write a Python program to find the length of each string in List1.

List1 = ['apple', 'banana', 'mango']

# Method 1: Basic for loop
print("Using for-loop:")
for fruit in List1:
    print(f"{fruit}: {len(fruit)}")

print()

# Method 2: List comprehension
lengths_lc = [len(fruit) for fruit in List1]
print("Using list comprehension:", lengths_lc)

# Method 3: map()
lengths_map = list(map(len, List1))
print("Using map():", lengths_map)

print()

# Method 4: Manual loop
def manual_len(s: str) -> int:
    count = 0
    for _ in s:
        count += 1
    return count

print("Using manual loop:")
for fruit in List1:
    print(f"{fruit}: {manual_len(fruit)}")

#15.Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition.

# List of strings
fruits = ["apple", "banana", "cherry", "mango", "orange"]

# String to search
search_item = "mango"

# Flag to check if found
found = False

# Loop through the list
for fruit in fruits:
    if fruit == search_item:
        found = True
        break

# Output result
if found:
    print(f"'{search_item}' found in the list.")
else:
    print(f"'{search_item}' not found in the list.")

#16.
# Define the number of lines
n = 5

# Outer loop: for each line i from 1 to n
for i in range(1, n + 1):
    # Inner loop: print '*' i times on the same line
    for j in range(i):
        print('*', end='')
    # After inner loop, move to next lineaa
    print()












