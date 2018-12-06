import random as rd

def err_sequence_1(item):
    item_list = list(item)

    err_pos1 = rd.randint(0,17)
    item_list[err_pos1] = str(int(item_list[err_pos1])^1)

    output_err_sequence = ''.join(item_list)
    return output_err_sequence

def err_sequence_23(item):
    item_list = list(item)
    err_num = rd.randint(2,4)
    err_pos1 = rd.randint(0,17)
    err_pos2 = rd.randint(0,17)
    err_pos3 = rd.randint(0,17)
    if(err_num==2):
        item_list[err_pos1] = str(int(item_list[err_pos1])^1)
        item_list[err_pos2] = str(int(item_list[err_pos2])^1)
    elif(err_num==3):
        item_list[err_pos1] = str(int(item_list[err_pos1])^1)
        item_list[err_pos2] = str(int(item_list[err_pos2])^1)
        item_list[err_pos3] = str(int(item_list[err_pos3])^1)

    output_err_sequence = ''.join(item_list)
    return output_err_sequence