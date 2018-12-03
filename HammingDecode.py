from HammingCode import noOfParityBits

# data = '001010110101111101'
def hammingDecode(data):
    # hc_item = '01101010101010101010'
    list_data = list(data)
    parity_num=noOfParityBits(len(data))
    loop_counter=0 #loop counter
    # parity_positon=1 #2 to the power kth parity bit
    while loop_counter<(parity_num-1):
        parity_positon=2**loop_counter-1
        list_data[parity_positon] = 'a'
        loop_counter = loop_counter+1
    while 'a' in list_data:
        list_data.remove('a')
    decoded_data = ''.join(list_data)
    print(decoded_data)
