import numpy as np

dhc_file = 'h2b.txt'
pre_shuffle_list = []

with open(dhc_file, 'r') as dhc_file_object:
    for dhc_item in dhc_file_object:
        dhc_item = dhc_item.rstrip()
        pre_shuffle_list.append(dhc_item)

# convert list to narray with numpy for data analysis
pre_shuffle_array = np.asarray(pre_shuffle_list)

print(pre_shuffle_array[:10])
# # fix the result for every shuffle
# np.random.seed(42)
# # randomly permutate the sequence of the data-set
# rnd_idx = np.random.permutation(60000)
# x_train = x_train[rnd_idx]
# y_train = y_train[rnd_idx]