import re

safe_lines = 0

with open("input") as input:
    for line in input:
        numbers = [int(number) for number in re.findall(r'[0-9]+', line)]
        differences = []
        for i in range(1, len(numbers)):
            differences.append(numbers[i - 1] - numbers[i])
        decreasing = all([i < 0 for i in differences])
        increasing = all([i > 0 for i in differences])
        changing_gradually = all([abs(i) <= 3 for i in differences])
        if changing_gradually and (decreasing or increasing):
            safe_lines += 1

print(safe_lines)