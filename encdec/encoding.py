import math
import os

from stegano import lsb


def split_string(s_str, count=10):
    per_c = math.ceil(len(s_str) / count)
    c_cout = 0
    out_str = ''
    split_list = []
    for s in s_str:
        out_str += s
        c_cout += 1
        if c_cout == per_c:
            split_list.append(out_str)
            out_str = ''
            c_cout = 0
    if c_cout != 0:
        split_list.append(out_str)
    print(split_list)
    return split_list


def encode_string(input_string, root):
    # for file in os.listdir(root):
    #     if file.endswith(".jpg"):
    split_string_list = split_string(input_string)
    for i in range(1, len(split_string_list)):
        secret_enc = lsb.hide("{}{}.png".format(root, i), split_string_list[i])
        secret_enc.save("{}{}.png".format(root, i))
        print("[INFO] frame {} holds {}".format(i, split_string_list[i]))
