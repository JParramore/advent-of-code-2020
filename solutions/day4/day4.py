import re

with open('input.txt') as input:
    passports = [re.split('\s', passport) for passport in input.read().split('\n\n')]

# PART 1/2

valid_rules = {'byr' : '^([1][9][2-9][0-9]|[2][0][0][0-2])$', 
                'iyr' : '^([2][0][1][0-9]|[2][0][2][0])$', 
                'eyr' : '^([2][0][2][0-9]|[2][0][3][0])$', 
                'hgt' : '([1][5][0-9]|[1][5-8][0-9]|[1][9][0-3]).*cm$|^([5][9]|[6][0-9]|[7][0-6]).*in$', 
                'hcl' : '^#[a-f0-9]{6}', 
                'ecl' : '(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)', 
                'pid' : '^[0-9]{9}$'
                }


def is_valid_passport(passport):
    for field in valid_rules:
        if field not in passport:
            return False
    return True

    
def is_valid_passport_two(passport):
    for field in valid_rules:
        if field not in passport:
            return False
        pattern = re.compile(valid_rules[field])
        if not pattern.match(passport[field]):
            return False
    return True


def get_passport(passport):
    passport_obj = {}
    for itentifier in passport:
        key = itentifier.split(':')[0]
        value = itentifier.split(':')[1]
        passport_obj[key] = value
    return passport_obj


def check_passports(passports):
    valid = 0
    valid_two = 0
    for passport in passports:
        if is_valid_passport(get_passport(passport)):
            valid += 1
        if is_valid_passport_two(get_passport(passport)):
            valid_two += 1
    
    print(f'valid passports: {valid}')
    print(f'valid passports part 2: {valid_two}')

check_passports(passports)