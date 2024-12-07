file = open("day07/input.txt", "r").read()
lines = str.split(file, "\n")

valid = []
for line in lines:
    target, vals = str.split(line, ':')
    target = int(target)
    vals = [int(x) for x in str.split(vals.strip(), ' ')]
    results = [vals[0]] 
    for i in range(1, len(vals), 1):
        temp = []
        for result in results:
            temp.append(result + vals[i])
            temp.append(result * vals[i])
        results = temp
    if target in results:
        valid.append(target)
        
print(sum(valid))

# Part two

valid = []
for line in lines:
    target, vals = str.split(line, ':')
    target = int(target)
    vals = str.split(vals.strip(), ' ')
    results = [vals[0]] 
    for i in range(1, len(vals), 1):
        temp = []
        for result in results:
            temp.append(int(result) + int(vals[i]))
            temp.append(int(result) * int(vals[i]))
            temp.append(int(str(result) + vals[i]))
        results = temp
    if target in results:
        valid.append(target)

print(sum(valid))