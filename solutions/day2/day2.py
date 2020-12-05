with open('input.txt') as input:
    entries = input.read().split('\n')

# PART 1

counter = 0

for entry in entries:
    parts = entry.split()

    char_range = parts[0].split('-')
    char = parts[1][0]
    password = parts[2]

    occurances = password.count(char)

    if occurances >= int(char_range[0]) and occurances <= int(char_range[1]):
        counter += 1

print(counter)

# PART 2

counter = 0
    
for entry in entries:
    parts = entry.split()

    char_range = parts[0].split('-')
    char = parts[1][0]
    password = parts[2]

    first_pos_char = password[int(char_range[0])-1]
    second_pos_char = password[int(char_range[1])-1]

    if (first_pos_char == char) ^ (second_pos_char == char):
        counter +=1

print(counter)