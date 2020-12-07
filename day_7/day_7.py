# %%
def rule_to_dict(rule: str):
    """
    convert one bag rule to a dict
    :param lst:
    :param sep:
    :return:
    """

    rule_scrubbed = rule.replace(' bags', '').replace('bag', '')
    outer_bag, inner_bags = rule_scrubbed.split('contain')
    inner_bags = inner_bags.lstrip(' ').rstrip('.').split(', ')
    inner_bags = dict(qty_type_str_key_val_pair(bag) for bag in inner_bags)
    return {outer_bag.strip(): inner_bags}


def qty_type_str_key_val_pair(string):
    """
    '1 bright white' -> ('bright white', 1)
    :return: 
    """
    string = string.strip()
    if string == 'no other':
        return string, 0
    else:
        return string[2:], int(string[0])


def get_rules_dict(rules):
    """
    generate rules dict out of rules list
    :param rules:
    :return:
    """
    rules_dict = dict()
    for rule in rules:
        rules_dict = {**rules_dict, **dict(rule_to_dict(rule))}
    return rules_dict


def find_bag(bag, parent_bag, rules: dict):
    """
    Recursively find if a bag is within another bag
    :param bag:
    :param parent_bag:
    :param rules:
    :return:
    """
    if bag in rules[parent_bag].keys():
        return True
    elif 'no other' in rules[parent_bag].keys():
        return False
    else:
        for parent_bag in rules[parent_bag]:
            if find_bag(bag, parent_bag, rules):
                return True


def find_number_bags_that_contain_specific_bag(bag, parent_bags, rules):
    """
    Recursively find number of bags within a bag
    :param bag: 
    :param parent_bags: 
    :param rules: 
    :return: 
    """
    count = 0
    for parent_bag in parent_bags:
        if find_bag(bag, parent_bag, rules):
            count += 1
    return count


def bag_count_within_bag(bag, rules):
    """
    Count number of bags with in bags
    :param bag:
    :param rules:
    :return:
    """
    count = 0
    for key, value in rules[bag].items():
        if key == 'no other':
            return value
        else:
            count += value + value * bag_count_within_bag(key, rules)
    return count


# %%

sample_input = [
    'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    'bright white bags contain 1 shiny gold bag.',
    'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    'faded blue bags contain no other bags.',
    'dotted black bags contain no other bags.'
]

sample_input2 = [
    'shiny gold bags contain 2 dark red bags.',
    'dark red bags contain 2 dark orange bags.',
    'dark orange bags contain 2 dark yellow bags.',
    'dark yellow bags contain 2 dark green bags.',
    'dark green bags contain 2 dark blue bags.',
    'dark blue bags contain 2 dark violet bags.',
    'dark violet bags contain no other bags.'
]

filename = "day_7/input.txt"
with open(filename) as f:
    input_data = f.readlines()

input_data = [(x.strip()) for x in input_data]

# %%
# part 1

bag_rules = get_rules_dict(input_data)
search_bag = 'shiny gold'
ans = find_number_bags_that_contain_specific_bag(search_bag, bag_rules.keys(), bag_rules)
print(f'Bag colors that eventually contain at least one shiny gold bag: {ans}')

# %%
# part 2

bag_rules = get_rules_dict(input_data)
search_bag = 'shiny gold'
ans = bag_count_within_bag(search_bag, bag_rules)
print(f'Individual bags that are required inside your single shiny gold bag: {ans}')
