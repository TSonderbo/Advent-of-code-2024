import re
file = open("day03/input.txt", "r").read()
muls = re.findall(r"mul\(\d*,\d*\)", file)
total = 0
for mul in muls:
    a, b = re.findall(r"\d+", mul)
    total += int(a) * int(b)
print(total)

# Part two

file = open("day03/input.txt", "r").read()
muls = re.findall(r"don't\(\)|do\(\)|mul\(\d*,\d*\)", file)
total = 0
skip = False
for mul in muls:
    if mul == "do()":
        skip = False
        continue
    elif mul == "don't()":
        skip = True
        continue
    if(skip):
        continue
    a, b = re.findall(r"\d+", mul)
    total += int(a) * int(b)
print(total)