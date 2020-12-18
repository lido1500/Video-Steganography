import math

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
    split_string_list = split_string(input_string)
    # for i in range(0, len(split_string_list)):
    # f_name = "{}frame{}.jpg".format(root, i)
    f_name = root
    # secret_enc = lsb.hide(f_name, split_string_list[i])
    secret_enc = lsb.hide(f_name, input_string)
    secret_enc.save(f_name)
    # print("[INFO] frame {} holds {}".format(f_name, split_string_list[i]))
    print("[INFO] frame {} holds {}".format(f_name, input_string))


if __name__ == "__main__":
    encode_string('secret', '/Users/pasang/vid_frames/0.png')
