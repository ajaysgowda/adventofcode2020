#%%
import numpy as np

#%%
sample_input = ['..##.......',
                '#...#...#..',
                '.#....#..#.',
                '..#.#...#.#',
                '.#...##..#.',
                '..#.##.....',
                '.#.#.#....#',
                '.#........#',
                '#.##...#...',
                '#...##....#',
                '.#..#...#.#']

# read input data

filename = "day_3/input.txt"
with open(filename) as f:
    input_data = f.readlines()

input_data = [(x.strip()) for x in input_data]


#%%
def get_nth_ele(data, n):
    """
    get the nth element in a iterable that never ends
    :param data:
    :return:
    """
    data_len = len(data)
    pos = n % data_len
    return data[pos]


def count_trees_in_path(data, c_move, r_move):
    """
    func that traverses the data and returns the tree count

    :param data: input data
    :param c_move: column move aka right movement
    :param r_move: row movement aka down movement
    :return: tree count
    """
    row_no = r_move
    col_no = c_move
    tree_count = 0
    while row_no < len(data):
        if get_nth_ele(data[row_no], col_no) == "#":
            tree_count += 1
        row_no += r_move
        col_no += c_move
    return tree_count


#%% part 1
trees = count_trees_in_path(data=input_data, c_move=3, r_move=1)

print(f'Trees in path:{trees}')

#%% part 2

directions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]  # (right_move, down_move)

tree_counts = []

for direction in directions:
    tree_counts.append(count_trees_in_path(input_data, *direction))

ans = np.prod(tree_counts)
print(f'Product of trees in path:{ans}')
