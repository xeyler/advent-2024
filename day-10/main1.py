# Identify each trailhead
grid = []
with open("input") as input:
    for line in input:
        grid.append([int(height) for height in line.rstrip()])

trailheads = set()

for x, line in enumerate(grid):
    for y, height in enumerate(line):
        if height == 0:
            trailheads.add((x, y))

# Compute the score of each trailhead
scores = []
for trailhead in trailheads:
    peaks = set()
    paths = [trailhead]
    while len(paths):
        x, y = paths.pop()
        height = grid[x][y]
        if height == 9:
            peaks.add((x, y))
        if x > 0 and grid[x-1][y] == height + 1:
            paths.append((x-1, y))
        if x < len(grid) - 1 and grid[x+1][y] == height + 1:
            paths.append((x+1, y))
        if y > 0 and grid[x][y-1] == height + 1:
            paths.append((x, y-1))
        if y < len(grid[0]) - 1 and grid[x][y+1] == height + 1:
            paths.append((x, y+1))
    scores.append(len(peaks))

# Sum the scores of all trailheads
print(sum(scores))
