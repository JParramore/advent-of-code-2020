with open('input.txt') as input:
    instructions = input.read().split('\n')

# PART 1

def is_valid_instructions(instructions):
    acc = 0
    visited = set()
    i = 0
    valid = False

    while i not in visited:
        if i == len(instructions):
            valid = True
            print('program terminated successfully')
            return valid, acc

        if i > len(instructions):
            print('out of range')
            return valid, acc

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
    
    return valid, acc


# PART 2

def find_switched_instruction(instructions):
    acc = 0
    valid = False
    
    for i, instruction in enumerate(instructions):
        new_instructions = instructions.copy()

        if instruction.split()[0] == 'jmp':
            new_instructions[i] = instruction.replace('jmp','nop')
            valid, acc = is_valid_instructions(new_instructions)
            if valid:
                return valid, acc

        elif instruction.split()[0] == 'nop':
            new_instructions[i] = instruction.replace('nop','jmp')
            valid, acc = is_valid_instructions(new_instructions)
            if valid:
                return valid, acc
        
    return valid, acc

print(is_valid_instructions(instructions))
print(find_switched_instruction(instructions))