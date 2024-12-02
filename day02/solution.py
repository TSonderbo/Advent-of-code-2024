file = open("day02/input.txt", "r").read()
lines = str.split(file, "\n")

safe = 0
for line in lines:
    values = [int(x) for x in line.split(" ")]
    p = sorted(values) == values or sorted(values, reverse=True) == values
    if p:
        valid = True
        for i in range(len(values)-1):
            dif = abs(int(values[i]) - int(values[i + 1]))
            if(dif not in (1, 2, 3)):
                valid = False
        if valid:
            safe += 1
print(safe)

# Part two

def check(values):
    p = sorted(values) == values or sorted(values, reverse=True) == values
    if p:
        valid = True
        for i in range(len(values)-1):
            dif = abs(int(values[i]) - int(values[i + 1]))
            if(dif not in (1, 2, 3)):
                valid = False
        if valid:
            return True
    return False

safe = 0
for line in lines:
    values = [int(x) for x in line.split(" ")]
    copy = values.copy()

    for i in range(len(values)):
        values.pop(i)
        valid = check(values)
        if valid:
            safe += 1
            break
        else:
            values = copy.copy()
print(safe)