target = "XMAS"
directions = [
    (-1, -1), (-1,  0), (-1,  1),
    ( 0, -1),           ( 0,  1),
    ( 1, -1), ( 1,  0), ( 1,  1)
]

grid = []

with open("input") as input:
    for file_line in input:
        grid.append(file_line.strip())

width = len(grid)
height = len(grid[0])
lines = [[[axis * i for axis in direction] for i in range(0, len(target))] for direction in directions]

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

for x in range(0, width):
    for y in range(0, height):
        for line in lines:
            total += check_line(line, x, y)

print(total)
