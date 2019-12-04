import random

def get_matrix_of_clear_number(clear_number):
    # 得到输入数据对应的十六进制ASCII码矩阵
    dir = {0: [], 1: [], 2: [], 3: []}
    length = len(clear_number)
    for i in range(length):
        number = ord(clear_number[i])
        dir[i % 4].append(hex(number))
    return dir

def get_matrix_of_cipher_number():
    # 得到随机生成的密钥的十六进制矩阵
    dir_number = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    string = ''
    for i in range(16):
        number = int(random.random() * 16)
        if (number >= 10):
            number = dir_number[number]
        else:
            number = str(number)
        string = string + number

    dir = get_matrix_of_clear_number(string)
    return dir

def define_S_box(fir_num, last_num):
    # 定义S盒
    dir = {
        0: ['0x63', '0x7c', '0x77', '0x7b', '0xf2', '0x6b', '0x6f', '0xc5', '0x30', '0x01', '0x67', '0x2b',
            '0xfe', '0xd7', '0xab', '0x76'],
        1: ['0xca', '0x82', '0xc9', '0x7d', '0xfa', '0x59', '0x47', '0xf0', '0xad', '0xd4', '0xa2', '0xaf', '0x9c',
            '0xa4', '0x72', '0xc0'],
        2: ['0xb7', '0xfd', '0x93', '0x26', '0x36', '0x3f', '0xf7', '0xcc', '0x34', '0xa5', '0xe5', '0xf1', '0x71',
            '0xd8', '0x31', '0x15'],
        3: ['0x04', '0xc7', '0x23', '0xc3', '0x18', '0x96', '0x05', '0x9a', '0x07', '0x12', '0x80', '0xe2', '0xeb',
            '0x27', '0xb2', '0x75'],
        4: ['0x09', '0x83', '0x2c', '0x1a', '0x1b', '0x6e', '0x5a', '0xa0', '0x52', '0x3b', '0xd6', '0xb3', '0x29',
            '0xe3', '0x2f', '0x84'],
        5: ['0x53', '0xd1', '0x00', '0xed', '0x20', '0xfc', '0xb1', '0x5b', '0x6a', '0xcb', '0xbe', '0x39', '0x4a',
            '0x4c', '0x58', '0xcf'],
        6: ['0xd0', '0xef', '0xaa', '0xfb', '0x43', '0x4d', '0x33', '0x85', '0x45', '0xf9', '0x02', '0x7f',
            '0x50', '0x3c', '0x9f', '0xa8'],
        7: ['0x51', '0xa3', '0x40', '0x8f', '0x92', '0x9d', '0x38', '0xf5', '0xbc', '0xb6', '0xda', '0x21',
            '0x10', '0xff', '0xf3', '0xd2'],
        8: ['0xcd', '0x0c', '0x13', '0xec', '0x5f', '0x97', '0x44', '0x17', '0xc4', '0xa7', '0x7e', '0x3d',
            '0x64', '0x5d', '0x19', '0x73'],
        9: ['0x60', '0x81', '0x4f', '0xdc', '0x22', '0x2a', '0x90', '0x88', '0x46', '0xee', '0xb8', '0x14',
            '0xde', '0x5e', '0x0b', '0xdb'],
        10: ['0xe0', '0x32', '0x3a', '0x0a', '0x49', '0x06', '0x24', '0x5c', '0xc2', '0xd3', '0xac', '0x62', '0x91',
             '0x95', '0xe4', '0x79'],
        11: ['0xe7', '0xc8', '0x37', '0x6d', '0x8d', '0xd5', '0x4e', '0xa9', '0x6c', '0x56', '0xf4', '0xea', '0x65',
             '0x7a', '0xae', '0x08'],
        12: ['0xba', '0x78', '0x25', '0x2e', '0x1c', '0xa6', '0xb4', '0xc6', '0xe8', '0xdd', '0x74', '0x1f', '0x4b',
             '0xbd', '0x8b', '0x8a'],
        13: ['0x70', '0x3e', '0xb5', '0x66', '0x48', '0x03', '0xf6', '0x0e', '0x61', '0x35', '0x57', '0xb9', '0x86',
             '0xc1', '0x1d', '0x9e'],
        14: ['0xe1', '0xf8', '0x98', '0x11', '0x69', '0xd9', '0x8e', '0x94', '0x9b', '0x1e', '0x87', '0xe9', '0xce',
             '0x55', '0x28', '0xdf'],
        15: ['0x8c', '0xa1', '0x89', '0x0d', '0xbf', '0xe6', '0x42', '0x68', '0x41', '0x99', '0x2d', '0x0f', '0xb0',
             '0x54', '0xbb', '0x16']
    }
    return (dir[fir_num][last_num])

def define_inverse_S_box(fir_num, last_num):
    # 定义S逆盒
    dir = {
        0: ['0x52', '0x09', '0x6a', '0xd5', '0x30', '0x36', '0xa5', '0x38', '0xbf', '0x40', '0xa3', '0x9e', '0x81',
            '0xf3', '0xd7', '0xfb'],
        1: ['0x7c', '0xe3', '0x39', '0x82', '0x9b', '0x2f', '0xff', '0x87', '0x34', '0x8e', '0x43', '0x44', '0xc4',
            '0xde', '0xe9', '0xcb'],
        2: ['0x54', '0x7b', '0x94', '0x32', '0xa6', '0xc2', '0x23', '0x3d', '0xee', '0x4c', '0x95', '0x0b', '0x42',
            '0xfa', '0xc3', '0x4e'],
        3: ['0x08', '0x2e', '0xa1', '0x66', '0x28', '0xd9', '0x24', '0xb2', '0x76', '0x5b', '0xa2', '0x49', '0x6d',
            '0x8b', '0xd1', '0x25'],
        4: ['0x72', '0xf8', '0xf6', '0x64', '0x86', '0x68', '0x98', '0x16', '0xd4', '0xa4', '0x5c', '0xcc', '0x5d',
            '0x65', '0xb6', '0x92'],
        5: ['0x6c', '0x70', '0x48', '0x50', '0xfd', '0xed', '0xb9', '0xda', '0x5e', '0x15', '0x46', '0x57', '0xa7',
            '0x8d', '0x9d', '0x84'],
        6: ['0x90', '0xd8', '0xab', '0x00', '0x8c', '0xbc', '0xd3', '0x0a', '0xf7', '0xe4', '0x58', '0x05', '0xb8',
            '0xb3', '0x45', '0x06'],
        7: ['0xd0', '0x2c', '0x1e', '0x8f', '0xca', '0x3f', '0x0f', '0x02', '0xc1', '0xaf', '0xbd', '0x03', '0x01',
            '0x13', '0x8a', '0x6b'],
        8: ['0x3a', '0x91', '0x11', '0x41', '0x4f', '0x67', '0xdc', '0xea', '0x97', '0xf2', '0xcf', '0xce', '0xf0',
            '0xb4', '0xe6', '0x73'],
        9: ['0x96', '0xac', '0x74', '0x22', '0xe7', '0xad', '0x35', '0x85', '0xe2', '0xf9', '0x37', '0xe8', '0x1c',
            '0x75', '0xdf', '0x6e'],
        10: ['0x47', '0xf1', '0x1a', '0x71', '0x1d', '0x29', '0xc5', '0x89', '0x6f', '0xb7', '0x62', '0x0e', '0xaa',
             '0x18', '0xbe', '0x1b'],
        11: ['0xfc', '0x56', '0x3e', '0x4b', '0xc6', '0xd2', '0x79', '0x20', '0x9a', '0xdb', '0xc0', '0xfe', '0x78',
             '0xcd', '0x5a', '0xf4'],
        12: ['0x1f', '0xdd', '0xa8', '0x33', '0x88', '0x07', '0xc7', '0x31', '0xb1', '0x12', '0x10', '0x59', '0x27',
             '0x80', '0xec', '0x5f'],
        13: ['0x60', '0x51', '0x7f', '0xa9', '0x19', '0xb5', '0x4a', '0x0d', '0x2d', '0xe5', '0x7a', '0x9f', '0x93',
             '0xc9', '0x9c', '0xef'],
        14: ['0xa0', '0xe0', '0x3b', '0x4d', '0xae', '0x2a', '0xf5', '0xb0', '0xc8', '0xeb', '0xbb', '0x3c', '0x83',
             '0x53', '0x99', '0x61'],
        15: ['0x17', '0x2b', '0x04', '0x7e', '0xba', '0x77', '0xd6', '0x26', '0xe1', '0x69', '0x14', '0x63', '0x55',
             '0x21', '0x0c', '0x7d']

    }
    return (dir[fir_num][last_num])

def hex_to_int_number(hex_num, flag):
    # 十六进制矩阵转换为十进制矩阵
    number = int(hex_num, 16)
    int_num = number // 16
    int_re = number % 16
    if flag == 1:
        my_number = define_S_box(int_num, int_re)
    else:
        my_number = define_inverse_S_box(int_num, int_re)
    return my_number

def define_byte_subdtitution(dir_new_number, flag):
    # 定义字节代换
    dir_1 = {0: [], 1: [], 2: [], 3: []}
    for j in range(4):
        list_new = []
        list = dir_new_number[j]
        for k in range(4):
            new_num = hex_to_int_number(list[k], flag)
            list_new.append(new_num)
        dir_1[j] = list_new
    return dir_1

def define_line_shift(dir_clear_number):
    # 进行行移位操作
    for i in range(4):
        my_list = []
        list = dir_clear_number[i]
        for j in range(4):
            my_list.append(list[(j + i) % 4])
        dir_clear_number[i] = my_list
    return dir_clear_number

def define_line_inverse_shift(dir_clear_number):
    # 进行行移位的逆操作
    for i in range(4):
        my_list = []
        list = dir_clear_number[i]
        for j in range(4):
            my_list.append(list[(j + 4 - i) % 4])
        dir_clear_number[i] = my_list
    return dir_clear_number

def XOR(string_1, string_2):
    # 得到异或后的十进制结果
    decimal_result = 0
    for i in range(8):
        if string_1[i] != string_2[i]:
            decimal_result += 2 ** (7 - i)

    return decimal_result

def dex_to_int(string):
    # 得到数据二进制到十进制的转换
    my_result = 0
    for k in range(8):
        if string[k] == '1':
            my_result += 2 ** (7 - k)
    return my_result

def get_2(last_num):
    # 得到列混合中乘以2的结果
    last_num_copy = last_num
    last_num_copy = bin(last_num_copy)[2:].rjust(8, '0')
    judge_num = bin(last_num)[2:]
    judge_num = last_num_copy[0]
    last_num_copy = last_num_copy[1:]
    last_num_copy += '0'

    if judge_num == '1':
        string_judge = '00011011'
        last_num_copy = bin(XOR(string_judge, last_num_copy))[2:].rjust(8, '0')
    return last_num_copy

def define_column_rotation(dir_clear_number_copy):
    # 在列混合中先将列进行旋转
    dir_clear_number = {0: [], 1: [], 2: [], 3: []}
    for key, num in dir_clear_number_copy.items():
        list = num
        for i in range(4):
            dir_clear_number[i].append(list[i])
    return dir_clear_number

def define_column_hybrid(dir_clear_number_copy):
    # 进行列混合操作，得到对应的十六进制的矩阵
    dir_matrix = {
        0: [2, 3, 1, 1],
        1: [1, 2, 3, 1],
        2: [1, 1, 2, 3],
        3: [3, 1, 1, 2]
    }
    dir_clear_number = define_column_rotation(dir_clear_number_copy)
    dir_new_clear_number = {0: [], 1: [], 2: [], 3: []}

    for i in range(4):
        list_matrix = dir_matrix[i]
        list = []
        for j in range(4):
            list_num = dir_clear_number[j]
            string = ''
            my_string = '00000000'

            for k in range(4):
                if list_matrix[k] == 2:
                    string = get_2(list_num[k])
                if list_matrix[k] == 3:
                    string = get_2(list_num[k])
                    list_num_copy = bin(list_num[k])[2:].rjust(8, '0')
                    string = bin(XOR(string, list_num_copy))[2:].rjust(8, '0')
                if list_matrix[k] == 1:
                    string = bin(list_num[k])[2:].rjust(8, '0')
                my_string = bin(XOR(my_string, string))[2:].rjust(8, '0')
            my_result = dex_to_int(my_string)
            list.append(hex(my_result))
            dir_new_clear_number[i] = list
    return dir_new_clear_number

def define_inverse_column_hybrid(dir_clear_number_copy):
    # 进行列混合逆操作，得到对应的十六进制的矩阵
    dir_matrix = {
        0: [14, 11, 13, 9],
        1: [9, 14, 11, 13],
        2: [13, 9, 14, 11],
        3: [11, 13, 9, 14]
    }
    dir_clear_number = define_column_rotation(dir_clear_number_copy)

    dir_new_clear_number = {0: [], 1: [], 2: [], 3: []}
    for i in range(4):
        list_matrix = dir_matrix[i]
        list = []
        for j in range(4):
            list_num = dir_clear_number[j]
            string = ''
            my_string = '00000000'
            my_result = 0

            for k in range(4):
                if list_matrix[k] == 14:
                    string_1 = get_2(list_num[k])
                    string_1_int = dex_to_int(string_1)
                    string_2 = get_2(string_1_int)
                    string_2_int = dex_to_int(string_2)
                    string_3 = get_2(string_2_int)
                    string = bin(XOR(string_2, string_1))[2:].rjust(8, '0')
                    string = bin(XOR(string, string_3))[2:].rjust(8, '0')
                if list_matrix[k] == 11:
                    string_1 = get_2(list_num[k])
                    string_1_int = dex_to_int(string_1)
                    string_2 = get_2(string_1_int)
                    string_2_int = dex_to_int(string_2)
                    string_3 = get_2(string_2_int)

                    string_4 = bin(list_num[k])[2:].rjust(8, '0')
                    string = bin(XOR(string_3, string_1))[2:].rjust(8, '0')
                    string = bin(XOR(string, string_4))[2:].rjust(8, '0')

                if list_matrix[k] == 13:
                    string_1 = get_2(list_num[k])
                    string_1_int = dex_to_int(string_1)
                    string_2 = get_2(string_1_int)
                    string_2_int = dex_to_int(string_2)
                    string_3 = get_2(string_2_int)

                    string_4 = bin(list_num[k])[2:].rjust(8, '0')
                    string = bin(XOR(string_3, string_2))[2:].rjust(8, '0')
                    string = bin(XOR(string, string_4))[2:].rjust(8, '0')
                if list_matrix[k] == 9:
                    string_1 = get_2(list_num[k])
                    string_1_int = dex_to_int(string_1)
                    string_2 = get_2(string_1_int)
                    string_2_int = dex_to_int(string_2)
                    string_3 = get_2(string_2_int)

                    string_4 = bin(list_num[k])[2:].rjust(8, '0')
                    string = bin(XOR(string_3, string_4))[2:].rjust(8, '0')

                my_string = bin(XOR(my_string, string))[2:].rjust(8, '0')

            my_result = dex_to_int(my_string)
            list.append(hex(my_result))
            dir_new_clear_number[i] = list
    return dir_new_clear_number

def hex_to_int(dir_clear_number):
    # 将十六进制的矩阵转换为十进制的矩阵
    dir_clear_number_copy = {0: [], 1: [], 2: [], 3: []}
    for key, num in dir_clear_number.items():
        list = []
        for i in range(4):
            list.append(int(num[i], 16))
        dir_clear_number_copy[key] = list
    return dir_clear_number_copy

def get_4_double(i_num, num, dir_key):
    # 在轮密钥加中 ，得到4的倍数
    dir_R = {
        1: ['01', '00', '00', '00'],
        2: ['02', '00', '00', '00'],
        3: ['04', '00', '00', '00'],
        4: ['08', '00', '00', '00'],
        5: ['10', '00', '00', '00'],
        6: ['20', '00', '00', '00'],
        7: ['40', '00', '00', '00'],
        8: ['80', '00', '00', '00'],
        9: ['1B', '00', '00', '00'],
        10: ['36', '00', '00', '00']
    }
    list_R = dir_R[i_num // 4 + 1]
    list = []
    list_dir = dir_key[num - 1]
    # print(list_dir)
    for i in range(4):
        list.append(list_dir[(i + 1) % 4])

    for i in range(4):
        list_int = int(list[i], 16)
        line_number = list_int // 16
        row_number = list_int % 16

        list[i] = define_S_box(line_number, row_number)
    list_new = []
    for i in range(4):
        num_1 = int(list_R[i], 16)
        num_2 = int(list[i], 16)
        string_1 = bin(num_1)[2:].rjust(8, '0')
        string_2 = bin(num_2)[2:].rjust(8, '0')
        string = XOR(string_1, string_2)
        list_new.append(hex(string))
    return list_new

def get_extend_key(dir_cipher_number):
    # 得到扩展密钥
    dir_cipher_number_copy = dir_cipher_number

    dir_key = {}
    for i in range(44):
        dir_key[i] = []

    for j in range(4):
        list = []
        list_dir = dir_cipher_number_copy[j]
        for k in range(4):
            list.append(list_dir[k])
        dir_key[j] = list

    for i in range(40):
        num = 4 + i
        if num % 4 == 0:
            list_T = get_4_double(i, num, dir_key)
        else:
            list_T = dir_key[num - 1]

        list_key = dir_key[num - 4]
        list = []
        for j in range(4):
            string_1 = bin(int(list_T[j], 16))[2:].rjust(8, '0')
            string_2 = bin(int(list_key[j], 16))[2:].rjust(8, '0')
            string = XOR(string_1, string_2)
            list.append(hex(string))
        dir_key[4 + i] = list
    return dir_key

def get_round_key_plus(clear_number, dir_key_extend):
    # 进行轮密钥加的操作
    dir_new_number = {0: [], 1: [], 2: [], 3: []}
    for i in range(4):
        list_number = clear_number[i]
        list_key = dir_key_extend[i]
        list = []
        for j in range(4):
            number = int(list_number[j], 16)
            key = int(list_key[j], 16)
            string_num = bin(number)[2:].rjust(8, '0')
            string_key = bin(key)[2:].rjust(8, '0')
            result_int = XOR(string_num, string_key)
            list.append(hex(result_int))
        dir_new_number[i] = list
    return dir_new_number

def define_encryption(clear_number, dir_key_extend):
    # 对明文进行轮密钥加
    dir_new_number = get_round_key_plus(clear_number, dir_key_extend)

    # 进行中间的十轮运算
    for i in range(10):
        num = 4 * (i + 1)
        dir_key_extend_part = {}

        for j in range(4):
            dir_key_extend_part[j] = dir_key_extend[num]
            num += 1

        # 字节代换
        dir_1 = define_byte_subdtitution(dir_new_number, 1)

        # 行移位
        dir_1 = define_line_shift(dir_1)

        # 定义列混合操作
        if i != 9:
            dir_1 = hex_to_int(dir_1)
            dir_1 = define_column_hybrid(dir_1)

        # 定义轮密钥加
        dir_1 = get_round_key_plus(dir_1, dir_key_extend_part)
        dir_new_number = dir_1

    return dir_new_number

def define_decryption(clear_number, dir_key_extend):
    # 对密文进行轮密钥加
    dir_key_extend_part = {
        0: dir_key_extend[40],
        1: dir_key_extend[41],
        2: dir_key_extend[42],
        3: dir_key_extend[43]
    }
    dir_new_number = get_round_key_plus(clear_number, dir_key_extend_part)

    # 进行中间的十轮运算
    k = 9
    for i in range(10):
        num = 4 * k
        dir_key_extend_part = {}
        for j in range(4):
            dir_key_extend_part[j] = dir_key_extend[num]
            num += 1
        k -= 1

        # 逆行移位
        dir_1 = define_line_inverse_shift(dir_new_number)

        # 逆字节代换
        dir_1 = define_byte_subdtitution(dir_1, 0)

        # 定义轮密钥加
        dir_1 = get_round_key_plus(dir_1, dir_key_extend_part)
        dir_new_number = dir_1

        # 定义逆列混合操作
        if i != 9:
            dir_1 = hex_to_int(dir_1)
            dir_1 = define_inverse_column_hybrid(dir_1)
        dir_new_number = dir_1
    return dir_new_number

def print_(dir_num):
    # 测试输出字典
    for key, num in dir_num.items():
        print(num)

def get_outcome(dir_num):
    # 输出解密之后的内容
    dir_num = define_column_rotation(dir_num)
    string = ''
    for i in range(4):
        list_num = dir_num[i]
        for j in range(4):
            num = list_num[j]
            num = chr(int(num, 16))
            string += num
    return string

def get_standard_input(string):
    # 得到16个字符的输入
    length = len(string)
    length = 16 - length
    for i in range(length):
        string += '0'
    return string

if __name__ == "__main__":
    print("Enter numbers( 0 - 16 number, if less than 16, it will fill with '0' by default): ")
    clear_number = input()
    clear_number = get_standard_input(clear_number)

    # 得到明文矩阵
    dir_clear_number = get_matrix_of_clear_number(clear_number)

    print_(dir_clear_number)  # 输出明文矩阵
    print("\n")

    # 得到密文矩阵
    dir_cipher_number = get_matrix_of_cipher_number()

    # 得到扩展的密钥
    dir_key_extend = get_extend_key(dir_cipher_number)

    print(dir_key_extend)  # 输出扩展密钥
    print("\n")

    dir_new_encrypt_number = define_encryption(dir_clear_number, dir_key_extend)
    print_(dir_new_encrypt_number)  # 输出密文矩阵
    print("\n")

    dir_orinal_ = define_decryption(dir_new_encrypt_number, dir_key_extend)
    print_(dir_orinal_)  # 输出解密后的矩阵

    dir_ = get_outcome(dir_orinal_)
    print(dir_)  # 输出解密后的原文
