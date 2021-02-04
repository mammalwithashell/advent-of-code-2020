# Open input file and parse input
from typing import Counter


with open("Day 7\input.txt", 'r') as input_file:
    #print(input_file.readlines())
    rules = [line.strip() for line in input_file.readlines()]
    
rule_dict = {}
for rule in rules:
    
    color_index = rule.find("contain")
    color = rule[:color_index].strip()
    color = color[:color.find("bag")].strip()
    if rule[color_index:] == "contain no other bags.":
        rule_dict[color] = []
        continue
    contains_list = rule[color_index + 7:].strip()[:-1].split(",")
    contains_list = [color[:color.find("bag")].strip() for color in contains_list]
    contains_list = [color[2:] for color in contains_list]
    
    rule_dict[color] = contains_list.copy()
    
# find shiny gold bags at base level
count = 0
base_list = []
shiny_set = set()
for k, v in rule_dict.items():
    if "shiny gold" in v:
        shiny_set.add(k)
        base_list.append(k)

visited = set()
def shiny_find(colorToFind: str):
    global count
    visited.add(colorToFind)
    for k, v in rule_dict.items():
        if colorToFind in v and k not in visited:
            shiny_set.add(k)
            base_list.append(k)         
            
while(base_list):
    shiny_find(base_list.pop(0))

print(len(shiny_set))