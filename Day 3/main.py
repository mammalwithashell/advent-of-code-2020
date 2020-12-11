# Open input file and parse input
with open("Day 3\input.txt", 'r') as input_file:
    forest = [line.strip() for line in input_file.readlines()]

# initialize variables for x, y, width and # of trees
x, y, w, t = 0, 0, len(forest[0]), 0

# walk the forest and loop around the right side
while(y < len(forest)):
    t += forest[y][x % w] == "#"
    x += 3
    y += 1

print(t)
    