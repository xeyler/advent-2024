diskmap = list()

# read the first line of input and make it a list of single-digit ints
with open('input') as input:
    diskmap = list(map(int, input.readline()))

blocks = list()

for i, number in enumerate(diskmap, start=0):
    blocks += [None if i % 2 else int(i / 2)] * number

# move file blocks one at a time until all free space is to the right
left = 0
right = len(blocks) - 1
while True:
    while left < len(blocks) and blocks[left] != None:
        left += 1
    while right >= 0 and blocks[right] == None:
        right -= 1
    if left >= right:
        break
    blocks[left] = blocks[right]
    blocks[right] = None

# calculate the checksum
checksum = 0
for i, id in enumerate(blocks):
    if id:
        checksum += i * int(id)

print(checksum)
