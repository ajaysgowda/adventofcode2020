#%%

def split_data(input_data):
    """

    :param input_data:
    :return: tuple of (limits, rep_char, password)
    """
    data = input_data.split(' ')
    password = data[2]
    rep_char = data[1].strip(':')
    limits = tuple(map(int, data[0].split('-')))
    return limits, rep_char, password


def check_for_validity_puzzle_1(limits: tuple, rep_char: str, password: str):
    """
    Test for validity based on requirements
    :param limits:
    :param rep_char:
    :param password:
    :return:
    """

    reps = password.count(rep_char)

    lower, upper = limits

    if lower <= reps <= upper:
        return True
    else:
        return False


def number_of_valid_pass_puzzle_1(input_list: list):
    """
    count number of valid passwords in a list
    :param input_list:
    :return:
    """
    num_of_valid = 0
    for item in input_list:
        data = split_data(item)
        if check_for_validity_puzzle_1(*data):
            num_of_valid += 1
    return num_of_valid


def check_for_validity_puzzle_2(pos: tuple, char: str, password: str):
    """
    Test for validity based on requirements
    :param pos:
    :param char:
    :param password:
    :return:
    """

    valid_pos, invalid_pos = pos
    # using xor
    if (password[valid_pos-1] == char) ^ (password[invalid_pos-1] == char):
        return True
    else:
        return False


def number_of_valid_pass_puzzle_2(input_list: list):
    """
    count number of valid passwords in a list
    :param input_list:
    :return:
    """
    num_of_valid = 0
    for item in input_list:
        data = split_data(item)
        if check_for_validity_puzzle_2(*data):
            num_of_valid += 1
    return num_of_valid

#%%
# read input data

filename = "day_2/input.txt"
with open(filename) as f:
    input_data = f.readlines()

input_data = [(x.strip()) for x in input_data]

#%%
# test = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']

num_of_valid_pass_puzzle_1 = number_of_valid_pass_puzzle_1(input_data)

num_of_valid_pass_puzzle_2 = number_of_valid_pass_puzzle_2(input_data)






