
file = open("day06/input.txt", "r").read()
lines = str.split(file, "\n")

guard_pos = (0,0)
guard_pos_org = (0,0)
guard_map = {}
direction = '^'
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        guard_map[(i,j)] = char
        if(char == '^'):
            guard_pos = (i,j)
            guard_pos_org = (i,j)
            guard_map[(i,j)] = '.'
      
trace = set()
while(True):
    trace.add(guard_pos)
        
    if(direction == '^'):
        new_pos = (guard_pos[0] - 1, guard_pos[1])
        if(new_pos not in guard_map):
            break
        elif(guard_map[new_pos] == '#'):
            direction = '>'
        else:
            guard_pos = new_pos
    elif(direction == '>'):
        new_pos = (guard_pos[0], guard_pos[1] + 1)
        if(new_pos not in guard_map):
            break
        elif(guard_map[new_pos] == '#'):
            direction = 'v'
        else:
            guard_pos = new_pos
    elif(direction == 'v'):
        new_pos = (guard_pos[0] + 1, guard_pos[1])
        if(new_pos not in guard_map):
            break
        elif(guard_map[new_pos] == '#'):
            direction = '<'
        else:
            guard_pos = new_pos
    elif(direction == '<'):
        new_pos = (guard_pos[0], guard_pos[1] - 1)
        if(new_pos not in guard_map):
            break
        elif(guard_map[new_pos] == '#'):
            direction = '^'
        else:
            guard_pos = new_pos
    
print(len(trace))    

counter = 0
for pos in trace:
    direction = '^'
    guard_pos = guard_pos_org
    guard_map[(pos[0],pos[1])] = '#'
    loop = True
    for _ in range(2 * len(trace)):
        if(direction == '^'):
            new_pos = (guard_pos[0] - 1, guard_pos[1])
            if(new_pos not in guard_map):
                loop = False
                break
            elif(guard_map[new_pos] == '#'):
                direction = '>'
            else:
                guard_pos = new_pos
        elif(direction == '>'):
            new_pos = (guard_pos[0], guard_pos[1] + 1)
            if(new_pos not in guard_map):
                loop = False
                break
            elif(guard_map[new_pos] == '#'):
                direction = 'v'
            else:
                guard_pos = new_pos
        elif(direction == 'v'):
            new_pos = (guard_pos[0] + 1, guard_pos[1])
            if(new_pos not in guard_map):
                loop = False
                break
            elif(guard_map[new_pos] == '#'):
                direction = '<'
            else:
                guard_pos = new_pos
        elif(direction == '<'):
            new_pos = (guard_pos[0], guard_pos[1] - 1)
            if(new_pos not in guard_map):
                loop = False
                break
            elif(guard_map[new_pos] == '#'):
                direction = '^'
            else:
                guard_pos = new_pos
    counter += loop
    guard_map[(pos[0],pos[1])] = '.'
    
print(counter)