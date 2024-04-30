# Define the size choices
SIZE_CHOICES = ['S', 'M', 'L', 'XL', 'XXL']

# Generate combinations
combinations = []
for i in range(1, len(SIZE_CHOICES) + 1):
    for j in range(len(SIZE_CHOICES) - i + 1):
        combination = ''.join(SIZE_CHOICES[j:j+i])
        combinations.append(combination)

# Print the combinations
for combination in combinations:
    print(combination)

