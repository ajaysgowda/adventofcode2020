#%%
import itertools
import numpy as np
import time
filename = "day_1/input.txt"
with open(filename) as f:
    data_input = f.readlines()

data_input = [int(x.strip()) for x in data_input]


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
time_s = time.process_time()
sum_2_2020 = find_sum_of(data_input, 2020, 2)

ans = sum_2_2020.pop()

print(time.process_time()-time_s)
print(f'{ans} has sum of {sum(ans)} and product of {np.prod(ans)}')

#%%
# challange 2

time_s = time.process_time()
sum_3_2020 = find_sum_of(data_input, 2020, 3)

ans = sum_3_2020.pop()

print(time.process_time()-time_s)
print(f'{ans} has sum of {sum(ans)} and product of {np.prod(ans)}')

#%% fast part 1
time_s = time.process_time()

diff = [2020-x for x in data_input]

ans = set(diff).intersection(set(data_input))
print(time.process_time()-time_s)
print(f'{ans} has sum of {sum(ans)} and product of {np.prod(list(ans))}')



