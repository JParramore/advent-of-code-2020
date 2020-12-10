with open('input.txt') as input:
    instructions = input.read().split('\n')

# PART 1

def accumulated(instructions):
    acc = 0
    visited = set()
    i = 0

    while i not in visited:
        if i > len(instructions):
            break

        instruction = instructions[i].split()[0]
        amount = int(instructions[i].split()[1])

        if instruction == 'jmp':
            visited.add(i)
            i = i + amount
        if instruction == 'acc':
            acc = acc + amount
            visited.add(i)
            i += 1
        if instruction == 'nop':
            visited.add(i)
            i += 1
        
    return acc

print(accumulated(instructions))