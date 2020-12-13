from collections import defaultdict
import re

with open('input.txt') as input:
    rules = input.read().split('\n')

bags = defaultdict(dict)

for rule in rules:
    bag = rule.split(' bags contain ')[0]
    can_contain = re.findall(r'(\d+) (\w+ \w+)', rule)
    
    for num, contained in can_contain:
        bags[bag][contained] = int(num)


# PART 1

def find_outermost_bags(bags, target):
    bags_with_target = 0
    

    for bag in bags:
        bags_copy = bags.copy()
        if search(bags_copy, bag, target):
            bags_with_target += 1
        
    return bags_with_target - 1


def search(bags, bag, target):
    if bag == target:
        return True

    for inner_bag in bags[bag]:
        if search(bags, inner_bag, target):
            return True
    
    return False


 # PART 2

def count_individual_bags(bags, target):
    total_contained = 1

    for bag in bags[target]:
        number_of_bags = bags[target][bag]
        total_contained += number_of_bags * count_individual_bags(bags, bag)
        
    return total_contained


print(find_outermost_bags(bags,'shiny gold'))
print(count_individual_bags(bags, 'shiny gold'))