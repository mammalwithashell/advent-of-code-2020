# function to be ran multiple times for part 2
def travel_forest(x_slope, y_slope, map:list) -> int:
    # initialize variables for x, y, width and # of trees
    x, y, w, t = 0, 0, len(forest[0]), 0

    # walk the forest and loop around the right side
    while(y < len(forest)):
        t += forest[y][x % w] == "#"
        x += x_slope
        y += y_slope
        
    return t

# Open input file and parse input
with open("Day 3\input.txt", 'r') as input_file:
    forest = [line.strip() for line in input_file.readlines()]



print(travel_forest(3, 1, forest))
product = 1
for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    product *= travel_forest(slope[0], slope[1], map)

print(product)