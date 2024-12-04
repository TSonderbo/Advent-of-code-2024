import numpy as np
import re

file = open("day04/input.txt", "r").read()
lines : list[str] = str.split(file, "\n")
letters = np.matrix([list(x) for x in lines])

h_lines = letters.tolist() 
v_lines = letters.T.tolist()

diags = [letters[::-1,:].diagonal(i).A.ravel().tolist() for i in range(-letters.shape[0]+1,letters.shape[1])]
diags.extend(letters.diagonal(i).A.ravel().tolist() for i in range(letters.shape[1]-1,-letters.shape[0],-1))

counter = 0
for line in h_lines:
    counter += len(re.findall(r"XMAS", "".join(line)))
    counter += len(re.findall(r"XMAS", "".join(line)[::-1]))
for line in v_lines:
    counter += len(re.findall(r"XMAS", "".join(line)))
    counter += len(re.findall(r"XMAS", "".join(line)[::-1]))
for line in diags:
    counter += len(re.findall(r"XMAS", "".join(line)))
    counter += len(re.findall(r"XMAS", "".join(line)[::-1]))
print(counter)

# Part two

o1 = np.matrix([['M', '', 'M'],
                ['','A',''],
                ['S', '', 'S']])
o2 = o1.T
o3 = np.matrix(np.flipud(o1))
o4 = np.matrix(np.fliplr(o2))
counter = 0
for i in range(len(v_lines)):
    for j in range(len(h_lines)):
        try:
            slice = letters[i:i+3, j:j+3].copy()
            slice[1, 0] = ''
            slice[0, 1] = ''
            slice[2, 1] = ''
            slice[1, 2] = ''
            
            if (slice==o1).all() or (slice==o2).all() or (slice==o3).all() or (slice==o4).all():
                counter += 1
        except IndexError:
            pass

print(counter)
        
        
        
        
