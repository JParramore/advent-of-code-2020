with open('input.txt') as input:
    lines = input.read().split('\n')
    lines = [ int(line) for line in lines ]
lines += [max(lines) + 3]
lines += [0]
lines.sort()


# PART 1

def multiply_counts(lines):
    diffs = [lines[n] - lines[n-1] for n in range(1, len(lines))]
    return diffs.count(1) * diffs.count(3)


# PART 2

def count_arrangements(lines):
    diffs = [lines[n] - lines[n-1] for n in range(1, len(lines))]
    

    return ''

print(multiply_counts(lines))