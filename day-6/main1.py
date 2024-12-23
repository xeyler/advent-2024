import re

grid = []
guard_position = (0, 0)
width = 0
height = 0

with open("input") as input:
    for line in input:
        guard = re.search(r'\^|<|>|V', line)
        if guard:
            guard_position = (len(grid), guard.start())
        grid.append([character for character in line.rstrip()])

width = len(grid[0])
height = len(grid)

while guard_position[0] >= 0 and guard_position[0] < width and guard_position[1] >= 0 and guard_position[1] < height:
    cursor = grid[guard_position[0]][guard_position[1]]
    direction = (1, 0)
    match cursor:
        case '<':
            direction = (0, -1)
        case '^':
            direction = (-1, 0)
        case '>':
            direction = (0, 1)
        case 'V':
            direction = (1, 0)

    if guard_position[0] + direction[0] >= 0 and guard_position[0] + direction[0] < width and guard_position[1] + direction[1] >= 0 and guard_position[1] + direction[1] < height and grid[guard_position[0] + direction[0]][guard_position[1] + direction[1]] == '#':
        match cursor:
            case '<':
                grid[guard_position[0]][guard_position[1]] = '^'
            case '^':
                grid[guard_position[0]][guard_position[1]] = '>'
            case '>':
                grid[guard_position[0]][guard_position[1]] = 'V'
            case 'V':
                grid[guard_position[0]][guard_position[1]] = '<'
        continue

    grid[guard_position[0]][guard_position[1]] = 'X'

    if guard_position[0] + direction[0] >= 0 and guard_position[0] + direction[0] < width and guard_position[1] + direction[1] >= 0 and guard_position[1] + direction[1] < height:
        grid[guard_position[0] + direction[0]][guard_position[1] + direction[1]] = cursor

    guard_position = (guard_position[0] + direction[0], guard_position[1] + direction[1])

count = 0

for line in grid:
    for character in line:
        if character == 'X':
            count += 1

print(count)