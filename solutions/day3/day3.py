with open('input.txt') as input:
    terrain = input.read().split('\n')

# PART 1

trees = 0

for i, row in enumerate(terrain):
    if row[(i*3) % len(row)] == '#':
       trees += 1

print(trees)

# PART 2

def find_trees(right, down):
    trees = 0
    row = 0

    for i in range(0, len(terrain), down):
        if terrain[i][(row*right) % len(terrain[i])] == '#':
            trees += 1
        row += 1
    return trees

total_trees = find_trees(1, 1) * find_trees(3, 1) * find_trees(5, 1) * find_trees(7, 1) * find_trees(1, 2)
print(total_trees)