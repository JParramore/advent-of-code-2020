import string

with open('input.txt') as input:
    groups = [ person.split('\n') for person in input.read().split('\n\n') ]

# PART 1

def get_anyone(groups):
    count = 0

    for group in groups:
        answers = set()
        for person in group:
            answers.update(set(person))
        count += len(answers)

    return count

# PART 2

def get_everyone(groups):
    count = 0

    for group in groups:
        all_yes = set(string.ascii_lowercase)
        [ all_yes.intersection_update(set(person)) for person in group ]
        count += len(all_yes)

    return count


print(f'anyone answers yes count: {get_anyone(groups)}')
print(f'everyone answers yes count: {get_everyone(groups)}')