with open("Day 8\input.txt", 'r') as input_file:
    #print(input_file.readlines())
    instructions = [line.strip() for line in input_file.readlines()]

index = 0
visited = set()
accumulator = 0
while index not in visited:
    visited.add(index)
    instruction = instructions[index][:3]
    arg = int(instructions[index][4:])
    if instruction == "acc":
        accumulator += arg
    elif instruction == "jmp":
        index += arg
        continue
    index += 1
print(accumulator)