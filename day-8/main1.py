import itertools
import operator

grid = []
with open("input") as input:
    for line in input:
        grid.append([character for character in line.rstrip()])

antenna_map = {}

for x, line in enumerate(grid):
    for y, letter in enumerate(line):
        if letter != ".":
            if not letter in antenna_map:
                antenna_map[letter] = set()
            antenna_map[letter].add((x, y))

antinodes = set()

for antenna_set in antenna_map.values():
    for antenna_pair in itertools.permutations(antenna_set, 2):
        difference = tuple(map(operator.sub, *antenna_pair))
        antinode = tuple(map(operator.add, difference, antenna_pair[0]))
        antinodes.add(antinode)

antinodes_on_map = 0

# Remember! Not all antinodes are going to be on the map
for x, line in enumerate(grid):
    for y, letter in enumerate(line):
        if (x, y) in antinodes:
            antinodes_on_map += 1

print(antinodes_on_map)
