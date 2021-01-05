# Open input file and parse input
with open("Day 4\input.txt", 'r') as input_file:
    raw_passports = [line.strip() for line in input_file.readlines()]

# Borrowed from viliampucik on github
fields = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x.endswith("cm") and 150 <= int(x[:-2]) <= 193) or (x.endswith("in") and 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: re.fullmatch(r"#[\da-f]{6}", x),
    "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda x: re.fullmatch(r"\d{9}", x),
}

passport = {}
passports = []
for line in raw_passports:
    if line == "":
        passports.append(passport.copy())
        passport.clear()
    else:
        [passport.update({field.split(":")[0]:field.split(":")[1]}) for field in line.split()]

valid = 0
for p in passports:
    if len(p.keys()) == 8:
        valid += 1
    elif len(p.keys()) == 7 and "cid" not in p.keys():
        valid += 1

print(valid)