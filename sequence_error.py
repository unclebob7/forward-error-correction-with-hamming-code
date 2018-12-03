import random as rd

def err_sequence(item):
    item_list = list(item)
    err_num = rd.randint(1,3)
    err_pos1 = rd.randint(0,17)
    err_pos2 = rd.randint(0,17)
    if(err_num==1):
        # item_list[err_pos1] = str(7)
        item_list[err_pos1] = str(int(item_list[err_pos1])^1)
    elif(err_num==2):
        # item_list[err_pos1] = str(7)
        # item_list[err_pos2] = str(7)
        item_list[err_pos1] = str(int(item_list[err_pos1])^1)
        item_list[err_pos2] = str(int(item_list[err_pos2])^1)

    output_err_sequence = ''.join(item_list)
    return output_err_sequence
