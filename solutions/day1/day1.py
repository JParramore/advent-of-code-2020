target = 2020

with open('input.txt') as input:
    entries = [int(entry) for entry in input.read().split('\n')]

# PART 1

values = set()

for entry in entries:
    pair = target - entry
    if pair in values:
        print(f'{entry} + {pair} = {entry + pair}')
        print(f'{entry} * {pair} = {entry * pair}')
        break
    else:
        values.add(entry)

# PART 2

for i in range(len(entries)):
    for j in range(len(entries)-i):
        for l in range(len(entries)-i-j):
            total = entries[i] + entries[i+j] +  entries[i+j+l] 
            if total == target:
                answer = entries[i] * entries[i+j] * entries[i+j+l]
                print(answer)
                break