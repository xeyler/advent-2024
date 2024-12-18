import re

grid = []

with open("input") as input:
    for file_line in input:
        grid.append(file_line.strip())

width = len(grid)
height = len(grid[0])

def check_line(line, x, y):
    coordinates = [[point[0] + x, point[1] + y] for point in line]
    for i, coordinate in zip(range(len(coordinates)), coordinates):
        coord_x, coord_y = coordinate
        if coord_x < 0 or coord_x >= width:
            return False
        if coord_y < 0 or coord_y >= height:
            return False
        if grid[coord_x][coord_y] != target[i]:
            return False
    return True

total = 0

for x in range(0, width - 2):
    for y in range(0, height - 2):
        packed_string = grid[x][y] + grid[x][y+2] + grid[x+2][y] + grid[x+2][y+2] + grid[x+1][y+1]
        if re.match(r'(M(MS|SM)S|S(MS|SM)M)A', packed_string):
            total += 1

print(total)
