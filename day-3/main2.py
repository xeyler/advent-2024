import re

total = 0

with open("input") as input:
    # TODO: python match regex across multiple lines?
    for mul_enabled_section in re.findall(r'(?:^|do\(\))(.+?)(?:$|don\'t\(\))', input.read().replace('\n', '')):
        for mul in re.findall(r'mul\(([0-9]+),([0-9]+)\)', mul_enabled_section):
            total += int(mul[0]) * int(mul[1])

print(total)