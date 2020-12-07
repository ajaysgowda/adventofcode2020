#%%
from itertools import groupby


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


def number_positive_ans_per_group(lst: list):
    """
    return number of positive ans from a group
    :param lst:
    :return:
    """
    sets = map(set, lst)
    positive_ans = set.union(*sets)
    return len(positive_ans)


def sum_of_all_group_positive_ans(lst: list):
    """
    return the sum of all group positive ans
    :param lst:
    :return:
    """

    count = 0
    for item in lst:
        count += number_positive_ans_per_group(item)
    return count


def number_of_common_ans_per_group(lst: list):
    """
    return number of common ans among group
    :param lst:
    :return:
    """
    sets = map(set, lst)
    common_ans = set.intersection(*sets)
    return len(common_ans)


def sum_of_all_group_common_ans(lst: list):
    """
    return the sum of all group positive ans
    :param lst:
    :return:
    """

    count = 0
    for item in lst:
        count += number_of_common_ans_per_group(item)
    return count


#%%
# read input data
sample_input = [
    'abc',
    '',
    'a',
    'b',
    'c',
    '',
    'ab',
    'ac',
    '',
    'a',
    'a',
    'a',
    'a',
    '',
    'b'
]

filename = "day_6/input.txt"
with open(filename) as f:
    input_data = f.readlines()

input_data = [(x.strip()) for x in input_data]

#%%
# part 1

grouped_data = sep_to_grouped_list(input_data, '')
ans = sum_of_all_group_positive_ans(grouped_data)

print(f'Total number of "yes" answers in each group: {ans}')


#%%
# part 2

grouped_data = sep_to_grouped_list(input_data, '')
ans = sum_of_all_group_common_ans(grouped_data)
print(f'Total number of common "yes" answers in each group: {ans}')

print(ans)
