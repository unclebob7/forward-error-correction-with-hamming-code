from HammingCode import noOfParityBits as parity_num_func
from HammingCode import noOfParityBitsInCode as test_func2
from HammingCode import hammingCodes as hc
from HammingDecode import hammingDecode as hd

print('E.g : #parity bits in (7, 4)Hamming code')
print('{0} {1}'.format(parity_num_func(13), test_func2(18)))

# original binary file
ori_file = 'mlk_b.txt'
# file that stores hamming-encoded data-set
hc_file  ='b2h.txt'
# file that stores decoded hamming-encoded data-set
dhc_file = 'h2b.txt'
item_sum = 0
binary_list = []
hamming_list = []
dhamming_list = []

# hamming-encoding processing
with open(ori_file) as ori_file_object:   #以文本(wt)形式写入操作
    for line in ori_file_object:
        # truncate ESC: '\n' from obj
        hc_item = hc(line.rstrip())
        # type coersion : obj in list to str
        str_item = [str(i) for i in hc_item]
        # type coersion : str_item in list to integral string
        integral_item = ''.join(str_item)
        # append integral item to a temp_list
        binary_list.append(integral_item)
        # item_sum = item_sum+1

# output temp_list item into hc_file
with open(hc_file, 'w') as hc_file_object:
    for hc_item in binary_list:
        hc_item = hc_item+'\n'
        hc_file_object.write(hc_item)

# E.g. demonstration for hamming-decoding
with open(dhc_file, 'w') as dhc_file_object:
    for hc_item in binary_list:
        dhc_item = hd(hc_item)
        dhc_item = dhc_item+'\n'
        dhc_file_object.write(dhc_item)
