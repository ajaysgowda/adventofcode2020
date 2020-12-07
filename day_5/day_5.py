#%%
from typing import Tuple
import operator


def upper_half(min_val, max_val) -> Tuple[int, int]:
    """
    return upper half
    :param min_val:
    :param max_val:
    :return:
    """
    min_val = int(min_val + (max_val - min_val) / 2)
    min_val = min_val + min_val % 2
    return min_val, max_val


def lower_half(min_val, max_val) -> Tuple[int, int]:
    """
    return lower half
    :param min_val:
    :param max_val:
    :return:
    """
    max_val = int(max_val - (max_val - min_val) / 2)
    return min_val, max_val


def modify_row_col(char, min_row, max_row, min_col, max_col):
    """
    mover the row/col max/min values according to char
    :param char:
    :param min_row:
    :param max_row:
    :param min_col:
    :param max_col:
    :return:
    """
    switcher = {
        'F': lower_half,
        'B': upper_half,
        'L': lower_half,
        'R': upper_half
    }

    if char in ['F', 'B']:
        min_row, max_row = switcher.get(char)(min_row, max_row)
        return min_row, max_row, min_col, max_col

    if char in ['R', 'L']:
        min_col, max_col = switcher.get(char)(min_col, max_col)
        return min_row, max_row, min_col, max_col


def get_final_row_col(char, min_val, max_val):
    """
    get final row / col values
    :param char:
    :param min_val:
    :param max_val:
    :return:
    """
    if char in ['B', 'R']:
        return max_val
    elif char in ['F', 'L']:
        return min_val


def get_seat_id(boarding_pass):
    """
    Get seat id from boarding pass
    :param boarding_pass:
    :return:
    """
    min_row, max_row, min_col, max_col = 0, 127, 0, 7
    row, col = None, None
    for i, char in enumerate(list(boarding_pass)):

        if i == 6:
            row = get_final_row_col(char, min_row, max_row)

        elif i == 9:
            col = get_final_row_col(char, min_col, max_col)

        else:
            min_row, max_row, min_col, max_col = modify_row_col(char, min_row, max_row, min_col, max_col)

    return row * 8 + col


def find_missing_seat(lst: list):
    """
    find missing seat
    :param lst:
    :return:
    """

    lst.sort()
    lst_set = set(lst)

    min_val = lst[0]
    max_val = lst[-1]

    full_set = {x for x in range(min_val, max_val+1)}

    return full_set.difference(lst_set).pop()


#%%
# read input data
sample_input = [
    'BFFFBBFRRR',
    'FFFBBBFRRR',
    'BBFFBBFRLL'
]

filename = "day_5/input.txt"
with open(filename) as f:
    input_data = f.readlines()

input_data = [(x.strip()) for x in input_data]


#%%
# part 1
max_seat_id = max(map(get_seat_id, input_data))
print(f'Highest seat ID on a boarding pass: {max_seat_id}')

#%%
# part 2

seat_ids = list(map(get_seat_id, input_data))
missing_seat_id = find_missing_seat(seat_ids)

print(f'The ID of your seat: {missing_seat_id}')


