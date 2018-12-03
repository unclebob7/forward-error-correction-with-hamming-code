from HammingCode import noOfParityBits as parity_num_func
from HammingCode import noOfParityBitsInCode as test_func2
from HammingCode import hammingCodes as hc
from HammingCode import hammingDecode as hd
#from HammingCode import hammingCorrection as hc


print('E.g : #parity bits in (7, 4)Hamming code')
print('{0} {1}'.format(parity_num_func(13), test_func2(18)))

# original binary file
ori_file = 'a2b.txt'
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
        #print(integral_item.rstrip())
        item_sum = item_sum+1

# output temp_list item into hc_file
with open(hc_file, 'w') as hc_file_object:
    for hc_item in binary_list:
        # hamming_list.append(hc_item)
        hc_item = hc_item+'\n'
        hc_file_object.write(hc_item)

with open(dhc_file, 'w') as dhc_file_object:
    for hc_item in binary_list:
        # repeat similiar sequence in section1
        dhc_item = hd(hc_item)
        # dhamming_list.append(dhc_item)
        dhc_item = dhc_item+'\n'
        dhc_file_object.write(dhc_item)

# def hammingDecode(data):
#     list_data = list(data)
#     parity_num=parity_num_func(len(data))
#     loop_counter=0 #loop counter
#     parity_positon=1 #2 to the power kth parity bit
#     while loop_counter<parity_num:
#         parity_positon=2.**loop_counter
#         del list_data[parity_positon-1]
#     decoded_data = ''.join(list_data)
#     return decoded_data
