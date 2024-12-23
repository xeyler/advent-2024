import re

first_numbers = []
second_numbers = []

with open('input') as input:
    for line in input:
        left, right = re.search(r'([0-9]*)   ([0-9]*)', line).groups()
        first_numbers.append(int(left))
        second_numbers.append(int(right))

first_numbers = sorted(first_numbers)
second_numbers = sorted(second_numbers)

assert len(first_numbers) == len(second_numbers)

total = 0

for left, right in zip(first_numbers, second_numbers):
    total += abs(left - right)

print(total)