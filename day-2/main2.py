import re

safe_lines = 0

def is_sequence_ok(numbers):
    differences = []
    for i in range(1, len(numbers)):
        differences.append(numbers[i] - numbers[i - 1])
    increasing = numbers[-1] - numbers[0] > 0
    ok = [(i > 0 if increasing else i < 0) and abs(i) <= 3 for i in differences]
    return all(ok)

with open("input") as input:
    for line in input:
        numbers = [int(number) for number in re.findall(r'[0-9]+', line)]
        combinations = [numbers]
        for i in range(0, len(numbers)):
            copy = numbers.copy()
            del copy[i]
            combinations.append(copy)
        if any([is_sequence_ok(combination) for combination in combinations]):
            safe_lines += 1
        
print(safe_lines)