file = open("day08/input.txt", "r").read()
lines = str.split(file, "\n")

anten_pos = {}
x_bound = len(lines[0])
y_bound = len(lines)
anti_positions = set()
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char != '.':
            anten_pos[(i,j)] = char
            anti_positions.add((i,j)) # part2
            
def valid_pos(pos, x_bound, y_bound):
    return pos[0] >= 0 and pos[0] < x_bound and pos[1] >= 0 and pos[1] < y_bound

for pos, atype in anten_pos.items():
    for other_pos, other_atype in anten_pos.items():
        if pos != other_pos and atype == other_atype:
            x_dif = pos[0] - other_pos[0]
            y_dif = pos[1] - other_pos[1]
            antipos = (pos[0] + x_dif, pos[1] + y_dif)
            # if valid_pos(antipos, x_bound, y_bound): #part1 
            #     anti_positions.add(antipos)
            while(valid_pos(antipos, x_bound, y_bound)): #part2
                anti_positions.add(antipos)
                antipos = (antipos[0] + x_dif, antipos[1] + y_dif)
                
print(len(anti_positions))