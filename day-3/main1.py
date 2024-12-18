import re

total = 0

with open("input") as input:
    for line in input:
        for mul in re.findall(r'mul\(([0-9]+),([0-9]+)\)', line):
            total += int(mul[0]) * int(mul[1])

print(total)