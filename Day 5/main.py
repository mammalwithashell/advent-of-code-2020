from pprint import pprint
"""# build array representation of seats
seats = []
for _ in range(128):
    row = []
    for i in range(8):
        row.append(i)
        seats.append(row.copy())"""
        
# Open input file and parse input
with open("Day 5\input.txt", 'r') as input_file:
    #print(input_file.readlines())
    seat_things = [line.strip() for line in input_file.readlines()]



seatids =[]
output = []
seats = [[True]*8 for _ in range(128)]
for instruction in seat_things:
    row = 0
    count = 0
    
    # upper and lower bound
    upper = 128
    lower = 0
    col_lower = 0
    col_upper = 8
    column = 0  
    for letter in instruction:
        if count == 7:
            if letter == "F":
                row = lower
            else:
                row = upper
        if count == 9:
            if letter == "R":
                column = col_upper
            else:
                column = col_lower + 1
                
        if letter in "FB":
            # finds number for row
            if letter == "F":
                upper -= (upper - lower)/2
            else:
                lower += (upper - lower)/2
        else:
            if letter == "R":
                # do something
                col_lower += (col_upper - col_lower)/2
            else:
                # L command
                col_upper -= (col_upper - col_lower)/2                
        count += 1
        

    # print(f"Instruction: {instruction}, Row: {row}, Column: {column}")
    output.append(f"Row: {row}, Column: {column}")
    seats[int(row -1)][int(column-1)] = False
    seatids.append((row -1)* 8 + column-1)
    
pprint(seats)
pprint(seatids)
            

# the answer for part 1 is max(seatids)
# the answer for part 2 is in the list of seats