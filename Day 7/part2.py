with open("Day 7\input.txt", 'r') as input_file:
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
    contains_list = [(color[2:], int(color[:2])) for color in contains_list]
    
    rule_dict[color] = contains_list.copy()

def inShinyGold(parent):
    count = 0
    if sum(n for _, n in rule_dict[parent]) != 0:
        count = sum(n for _, n in rule_dict[parent])
        for color, n in rule_dict[parent]:
            count += n * inShinyGold(color)
    return count

    

print(inShinyGold("shiny gold"))