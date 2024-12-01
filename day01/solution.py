file = open("day01/input.txt", "r").read()
pairs = str.split(file, "\n")
list_a = []
list_b = []
for pair in pairs:
    a, b = str.split(pair, "   ")
    list_a.append(int(a))
    list_b.append(int(b))
list_a = sorted(list_a)
list_b = sorted(list_b)    
solution = sum([abs(a - b) for a, b in zip(list_a, list_b)])
print(solution)

# Path Two
solution_2 = sum([a * list_b.count(a) for a in list_a])
print(solution_2)