with open('input.txt') as input:
    passes = input.read().split('\n')

def get_row(row_id):
    rows = [i for i, x in enumerate(range(128))]
    for char in row_id:
        if char == 'F':
            rows = rows[:int(len(rows)/2)]
        else:
            rows = rows[int(len(rows)/2):]

    return rows[0]


def get_col(col_id):
    cols = [i for i, x in enumerate(range(8))]
    for char in col_id:
        if char == 'L':
            cols = cols[:int(len(cols)/2)]
        else:
            cols = cols[int(len(cols)/2):
            ]
    return cols[0]


def get_seat_id(boarding_pass):
    row_instruction = boarding_pass[:7]
    col_instruction = boarding_pass[-3:]

    row = get_row(row_instruction)
    col = get_col(col_instruction)

    return row * 8 + col

# PART 1

def highest_seat_id(passes):
    highest_seat_id = 0
    for boarding_pass in passes:
        seat_id = get_seat_id(boarding_pass)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    return highest_seat_id

# PART 2

def find_missing_id(passes):

    occupied = []

    for boarding_pass in passes:
        occupied.append(get_seat_id(boarding_pass))

    occupied.sort()
    first_seat = occupied[0]

    for i, seat in enumerate(occupied):
        if i+first_seat != seat:
            return seat-1


print(f'highest seat id: {highest_seat_id(passes)}')
print(f'my seat: {find_missing_id(passes)}')