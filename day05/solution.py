
file = open("day05/input.txt", "r").read()
rules, lines = str.split(file, "\n\n")
rules = str.split(rules, "\n")
lines = str.split(lines, "\n")

def valid(rules, lines):
    
    valid_lines = []
    invalid_lines = []
    for line in lines:
        line_vals = str.split(line, ",")
        valid = True
        for i in range(len(line_vals)):
            for j in range(len(line_vals)):
                if i == j:
                    continue
                for rule in rules:
                    val, before = str.split(rule, "|")
                    if line_vals[i] == val and line_vals[j] == before:
                        if i > j:
                            valid = False
        if valid:
            valid_lines.append(line_vals)
        else:
            invalid_lines.append(line_vals)
        
    return valid_lines, invalid_lines
            
valid_lines, invalid_lines = valid(rules, lines)

import math

total = 0
for line in valid_lines:
    middle = math.floor(len(line) / 2)
    total += int(line[middle])
    
print(total)

# Part two

invalid_lines
for line in invalid_lines:
    invalid = True
    while(invalid):
        found_error = False
        for i in range(len(line)):
            for j in range(len(line)):
                if i == j:
                    continue
                for rule in rules:
                    val, before = str.split(rule, "|")
                    if line[i] == val and line[j] == before:
                        if i > j:
                            temp = line[i]
                            line[i] = line[j]
                            line[j] = temp
                            found_error = True
        if found_error == False:
            break
                                

total = 0
for line in invalid_lines:
    middle = math.floor(len(line) / 2)
    total += int(line[middle])
print(total)