import sys

def calculate_secret_number(secret_number):
    secret_number = (((((secret_number ^ (secret_number * 64)) % 16777216) ^ (((secret_number ^ (secret_number * 64)) % 16777216) // 32)) % 16777216) ^ (((((secret_number ^ (secret_number * 64)) % 16777216) ^ (((secret_number ^ (secret_number * 64)) % 16777216) // 32)) % 16777216) * 2048)) % 16777216
    return secret_number

def find_2000_number(initial_numbers):
    results = []
    for number in initial_numbers:
        secret_number = number
        # Simulate 2000 steps
        for _ in range(2000):
            secret_number = calculate_secret_number(secret_number)
        results.append(secret_number)
    return results

# Read data from standard input
data = sys.stdin.read()

# Process the data into a list of numbers
numbers = [int(x) for x in data.split()]

# Find the 2000th number
numbers_2000 = find_2000_number(numbers)

# Calculate the sum
sum_of_numbers = sum(numbers_2000)
print("Sum of 2000th numbers:", sum_of_numbers)
