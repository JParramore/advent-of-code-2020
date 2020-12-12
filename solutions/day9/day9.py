with open('input.txt') as input:
    lines = input.read().split('\n')
    lines = [int(line) for line in lines]

PREAMBLE = 25


# PART 1

def find_invalid_number(lines):
    for i in range(PREAMBLE, len(lines)):
        valid = valid_numbers(lines[i-PREAMBLE:i], lines[i])
        if not valid:
            return lines[i]

    return -1


# find two numbers in list that sum to target
def valid_numbers(numbers, sum):
    potentials = set(numbers)

    for num in potentials:
        new_pot = potentials.copy()
        new_pot.remove(num)
        target = sum - num
        if target in new_pot:
            return True
    return False


# PART 2

def sum_smallest_largest(lines):
    target = find_invalid_number(lines)
    start = 0
    end = 0
    sum = lines[0]

    while True:
        if sum < target:
            end += 1
            sum += lines[end]
        if sum > target:
            sum -= lines[start]
            start += 1
        if sum == target:
            largest = max(lines[start:end])
            smallest = min(lines[start:end])
            return largest + smallest


print(f'smallest and largest in range: {sum_smallest_largest(lines)}')
