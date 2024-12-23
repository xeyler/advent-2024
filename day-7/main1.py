import itertools

OPERATORS = ['+', '*']

count = 0

with open('input') as input:
  for line in input:
    target, operands = [number.strip() for number in line.split(':')]
    target = int(target)
    operands = list(map(int, operands.split(' ')))
    for operators in list(
        itertools.product(OPERATORS, repeat=len(operands) - 1)):
      operand_i = 0
      # eval would have been easier, but it doesn't evaluate math left-to-right. it evaluates it according to the order of mathematical operators
      result = operands[operand_i]
      while operand_i < len(operands) - 1:
        if operators[operand_i] == '+':
          result += operands[operand_i + 1]
        if operators[operand_i] == '*':
          result *= operands[operand_i + 1]
        operand_i += 1
      if result == target:
        count += result
        # Only count the first successful combination of operands and operators
        break

print(count)
