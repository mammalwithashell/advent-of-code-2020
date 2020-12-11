from operator import xor

with open("Day 2 Password Philosophy\input.txt", 'r') as input_file:
    passwords = input_file.readlines()

passwords = [i.split() for i in passwords]

def validate(lower:int, upper:int, char:str, password:str) -> bool:
    count = 0
    for letter in password:
        if letter == char:
            count += 1
    
    if count >= lower and count <= upper:
        return True
    return False

def validate2(lower:int, upper:int, char:str, password:str) -> bool:
    if (password[lower-1] == char ) != (password[upper-1] == char):
        return True
    return False
        

count = 0
for item in passwords:
    item[0] = item[0].split("-")
    item[0] = [int(i) for i in item[0]]

    item[1] = item[1][:-1]
    
    """if validate(item[0][0], item[0][1], item[1], item[2]):
        count += 1"""
        
    if validate2(item[0][0], item[0][1], item[1], item[2]):
        count += 1
    
    
print(count)