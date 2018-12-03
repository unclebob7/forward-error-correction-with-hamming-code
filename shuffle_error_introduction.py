import numpy as np
from HammingDecode import hammingDecode as hd

dhc_file = 'b2h.txt'
compromised_h_file = 'compromised_h.txt'
compromised_b_file = 'compromised_b.txt'
pre_shuffle_list = []
# aft_shuffle_array = []
order_sequence = np.linspace(0,366400, 366401, dtype=np.int)
shuffle_order_sequence = []

with open(dhc_file, 'r') as dhc_file_object:
    for dhc_item in dhc_file_object:
        dhc_item = dhc_item.rstrip()
        pre_shuffle_list.append(dhc_item)

# convert list to narray with numpy for data analysis
pre_shuffle_array = np.asarray(pre_shuffle_list)
print('total length of dataset:{0}'.format(len(pre_shuffle_array)))

# fix the result for every shuffle
np.random.seed(42)
# randomly permutate the sequence of dataset (variable)
rnd_idx = np.random.permutation(366401)
# shuffled order sequence of dataset (constant)
shuffle_order_sequence = order_sequence[rnd_idx]
print('after-shuffled order-sequence demonstration:', shuffle_order_sequence[:10])
# aft_shuffle_array = pre_shuffle_array[rnd_idx]
# print('pre-shuffle demonstration:', pre_shuffle_array[:5])
# print('after-shuffle demonstration:', aft_shuffle_array[:5])

# apply changes to pre-shuffled sequence (awaiting to be updated to percentage form)
pre_shuffle_array[shuffle_order_sequence[:100000]] = 0
compromised_output_list = list(pre_shuffle_array)

# output compromised file (binary form)
with open(compromised_h_file, 'w') as cbf_object:
    for comp_item in compromised_output_list:
        comp_item = comp_item+'\n'
        cbf_object.write(comp_item)

# output compromised file (float form)
with open(compromised_b_file, 'w') as cff_object:
    for hc_item in compromised_output_list:
        dhc_item = hd(hc_item)
        dhc_item = dhc_item+'\n'
        cff_object.write(dhc_item)
