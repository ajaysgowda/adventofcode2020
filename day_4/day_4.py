# %%
from itertools import groupby
from typing import List

# %%
# read input data
sample_input = [
    'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
    'byr:1937 iyr:2017 cid:147 hgt:183cm',
    '',
    'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
    'hcl:#cfa07d byr:1929',
    '',
    'hcl:#ae17e1 iyr:2013',
    'eyr:2024',
    'ecl:brn pid:760753108 byr:1931',
    'hgt:179cm',
    '',
    'hcl:#cfa07d eyr:2025 pid:166559648',
    'iyr:2011 ecl:brn hgt:59in'
]

filename = "day_4/input.txt"
with open(filename) as f:
    input_data = f.readlines()

input_data = [(x.strip()) for x in input_data]


# %%


def sep_to_grouped_list(lst: list, sep: str):
    """
    seperate list to smaller groups based on separator
    :param lst:
    :param sep:
    :return:
    """
    grouped_list = []
    for k, g in groupby(lst, key=lambda x: x == sep):
        if not k:
            grouped_list.append(list(g))
    return grouped_list


def convert_to_consistent_dict(lst: List[str], sep):
    """
    convert list of mixed split strings to one single dict
    using recursion
    :param lst:
    :param sep:
    :return:
    """
    r_dict = dict()
    for item in lst:
        sep_list = item.split(sep)
        if len(sep_list) > 1:
            r_dict = {**r_dict, **convert_to_consistent_dict(sep_list, sep)}
        else:
            k, v = item.split(':')
            r_dict[k] = v

    return r_dict


def convert_data_list_to_dict(data: List[str]):
    """
    convert input list to dicts of inport data

    :param data:
    :return:
    """
    lst = sep_to_grouped_list(data, '')
    data_list = list()
    for item in lst:
        data_list.append(convert_to_consistent_dict(item, ' '))
    return data_list


def check_valid_id_part_1(iden: dict, req_fields: set):
    """
    check for valid id
    :param iden:
    :param req_fields:
    :return:
    """
    keys = set(iden.keys())
    if req_fields.difference(keys):
        return False
    else:
        return True


def check_valid_id_part_2(iden: dict, req_fields: set):
    """
    check for valid id
    :param iden:
    :param req_fields:
    :return:
    """

    keys = set(iden.keys())
    if req_fields.difference(keys):
        return False
    else:
        for key, value in iden.items():
            if not field_validator(key, value):
                return False
        return True


def count_valid_ids(ids: List[dict], req_fields: set, part: str):
    """
    count valid ids
    :param ids:
    :param req_fields:
    :param part:
        part of chllange
    :return:
    """
    if part == 'part2':
        validator = check_valid_id_part_2
    else:
        validator = check_valid_id_part_1

    valid_id_count = 0
    for iden in ids:
        if validator(iden, req_fields):
            valid_id_count += 1

    return valid_id_count


def check_in_range(val, min_val, max_val):
    """

    :param val:
    :param min_val:
    :param max_val:
    :return:
    """
    if min_val <= val <= max_val:
        return True
    else:
        return False


def validate_byr(val: str):
    """
    (Birth Year) - four digits; at least 1920 and at most 2002.
    :param val:
    :return:
    """
    min_val = 1920
    max_val = 2002
    return check_in_range(int(val), min_val, max_val)


def validate_iyr(val: str):
    """
    (Issue Year) - four digits; at least 2010 and at most 2020.
    
    :param val:
    :return:
    """
    min_val = 2010
    max_val = 2020
    return check_in_range(int(val), min_val, max_val)


def validate_eyr(val: str):
    """
    (Expiration Year) - four digits; at least 2020 and at most 2030.

    :param val:
    :return:
    """
    min_val = 2020
    max_val = 2030
    return check_in_range(int(val), min_val, max_val)


def validate_hgt(val: str):
    """
    (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.

    :param val:
    :return:
    """
    if 'cm' in val:
        return check_in_range(int(val[:-2]), 150, 193)
    elif 'in' in val:
        return check_in_range(int(val[:-2]), 59, 76)
    else:
        return False


def validate_hcl(val: str):
    """
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.

    :param val:
    :return:
    """
    val_list = list(val)
    if val_list.pop(0) == "#":
        if len(val_list) == 6:
            for item in val_list:
                is_0_9 = check_in_range(ord(item), ord('0'), ord('9'))
                is_a_f = check_in_range(ord(item), ord('a'), ord('f'))
                if is_0_9 or is_a_f:
                    return True
    else:
        return False


def validate_ecl(val: str):
    """
    (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.

    :param val:
    :return:
    """
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if val in colors:
        return True
    else:
        return False


def validate_pid(val: str):
    """
    (Passport ID) - a nine-digit number, including leading zeroes.

    :param val:
    :return:
    """
    if len(val) == 9:
        return True
    else:
        return False


def field_validator(key, val):
    switcher = {
        'byr': validate_byr,
        'iyr': validate_iyr,
        'eyr': validate_eyr,
        'hgt': validate_hgt,
        'hcl': validate_hcl,
        'ecl': validate_ecl,
        'pid': validate_pid
    }

    return switcher.get(key, lambda x: True)(val)


# %%
# part 1

id_dict = convert_data_list_to_dict(input_data)

required_fields = {'pid', 'iyr', 'eyr', 'hgt', 'byr', 'ecl', 'hcl'}
valid_p1 = count_valid_ids(id_dict, required_fields, part='part1')

print(f'Valid passports: {valid_p1}')

# %%
# part 2

id_dict = convert_data_list_to_dict(input_data)

required_fields = {'pid', 'iyr', 'eyr', 'hgt', 'byr', 'ecl', 'hcl'}
valid_p2 = count_valid_ids(id_dict, required_fields, part='part2')
print(f'Valid passports: {valid_p2}')
