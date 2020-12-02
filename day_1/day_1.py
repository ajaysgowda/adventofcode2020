#%%
import itertools
import numpy as np
filename = "day_1/input.txt"
with open(filename) as f:
    input = f.readlines()

input = [int(x.strip()) for x in input]

#%%

def find_sum_of(numbers, summ, n):
    """

    :param numbers: list of numbers
    :param summ: value of sum to track
    :param n: how many numbers to make the sum
    :return:
    """
    return [tup for tup in itertools.combinations(numbers, n) if sum(tup) == summ]

#%%
# challenge 1

sum_2_2020 = find_sum_of(input, 2020, 2)

ans = sum_2_2020.pop()

print(f'{ans} has sum of {sum(ans)} and product of {np.prod(ans)}')

#%%
# challange 2

sum_3_2020 = find_sum_of(input, 2020, 3)

ans = sum_3_2020.pop()

print(f'{ans} has sum of {sum(ans)} and product of {np.prod(ans)}')


