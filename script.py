# Define the size of the pattern
size = 10

# Loop to print the upper half of the pattern
for i in range(size):
    print((' ' * (size - i - 1)) + ('* ' * (i + 1)))

# Loop to print the lower half of the pattern
for i in range(size - 1):
    print((' ' * (i + 1)) + ('* ' * (size - i - 1)))
