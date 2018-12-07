import numpy as np
from HammingDecode import hammingDecode as hd
from sequence_error import err_sequence_1,err_sequence_23
from HammingCode import hammingCorrection as hc

dhc_file = 'b2h.txt'
compromised_h_file = 'compromised_h.txt'
compromised_b_file = 'compromised_b.txt'
fec_b_file = 'fec_b.txt'
pre_shuffle_list = []
# aft_shuffle_array = []
order_sequence = np.linspace(0,284443, 284444, dtype=np.int)
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
rnd_idx = np.random.permutation(284444)
# shuffled order sequence of dataset (constant)
shuffle_order_sequence = order_sequence[rnd_idx]
print('after-shuffled order-sequence demonstration:', shuffle_order_sequence[:10])


# apply changes to pre-shuffled sequence (awaiting to be updated to percentage form)
# pre_shuffle_array[shuffle_order_sequence[:100000]] = 0
# compromised_output_list = list(pre_shuffle_array)

# pre_shuffle_list = list(pre_shuffle_array[shuffle_order_sequence[:100000]])

"""introduce 1-bit error"""
for item in shuffle_order_sequence[:1500]:
    pre_shuffle_array[item] = err_sequence_1(pre_shuffle_array[item])

"""introduce 2 or 3-bit error"""
for item in shuffle_order_sequence[1500:2500]:
    pre_shuffle_array[item] = err_sequence_23(pre_shuffle_array[item])
compromised_output_list = list(pre_shuffle_array)

# output compromised file (18 form)
with open(compromised_h_file, 'w') as cbf_object:
    for comp_item in compromised_output_list:
        comp_item = comp_item+'\n'
        cbf_object.write(comp_item)

# output compromised file (13 form)
with open(compromised_b_file, 'w') as cff_object:
    for hc_item in compromised_output_list:
        dhc_item = hd(hc_item)
        dhc_item = dhc_item+'\n'
        cff_object.write(dhc_item)

"""rectify 1-bit error from 1-bit error introduction"""
for item in shuffle_order_sequence[:1500]:
    chc_list_item = hc(pre_shuffle_array[item])
    chc_list_item = [str(i) for i in chc_list_item]
    chc_str_item = ''.join(chc_list_item)
    pre_shuffle_array[item] = chc_str_item

"""decode the rest from hammming"""
for item in shuffle_order_sequence[1500:]:
    pre_shuffle_array[item] = hd(pre_shuffle_array[item])
rectified_output_list = list(pre_shuffle_array)


# output fec file in de-hamming form (13)
with open(fec_b_file,'w') as fec_b_object:
    for rectified_item in rectified_output_list:
        rectified_item = rectified_item+'\n'
        fec_b_object.write(rectified_item)
