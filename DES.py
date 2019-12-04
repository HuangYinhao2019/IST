base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]

#2 to 10
def bin2dec(string_num):
    return str(int(string_num, 2))
#16 to 10
def hex2dec(string_num):
    return str(int(string_num.upper(), 16))
#10 to 2
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])
#10 to 16
def dec2hex(string_num):
    num = int(string_num)
    if num == 0:
        return '0'
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])
#16 to 2
def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))
#2 to 16
def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))

subKey = [([0] * 48) for _ in range(16)]

#S1
s1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
#IP置换
ip = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
#逆IP
_ip = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
       38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
       36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
       34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

LS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
#ip 置换
def changeIP(source):
    dest = [0] * 64
    global ip
    for i in range(64):
        dest[i] = source[ip[i] - 1]
    return dest

def string2Binary(str):
    le = len(str)
    dest = [0] * le * 4
    i = 0
    for c in str:
        i += 4
        j = 0
        s = hex2bin(c)
        l = len(s)
        for d in s:
            dest[i - l + j] = int(d)
            j += 1
    return dest
#逆ip 置换
def changeInverseIP(source):
    dest = [0] * 64
    global _ip
    for i in range(64):
        dest[i] = source[_ip[i] - 1]

    return dest

def setKey(source):
    global subKey
    # 装换4bit
    temp = string2Binary(source)
    # 6bit均分成两部分
    left = [0] * 28
    right = [0] * 28
    # 经过PC-14bit转换6bit
    temp1 = [0] * 56
    temp1 = keyPC_1(temp)
    # printArr(temp1);
    # 将经过转换的temp1均分成两部分
    for i in range(28):
        left[i] = temp1[i]
        right[i] = temp1[i + 28]
    # 经过16次循环左移，然后PC-2置换
    for i in range(16):
        left = keyLeftMove(left, LS[i])
        right = keyLeftMove(right, LS[i])
        for j in range(28):
            temp1[j] = left[j]
            temp1[j + 28] = right[j]
        subKey[i] = keyPC_2(temp1)

def keyPC_2(source):
    dest = [0] * 48
    temp = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]
    for i in range(48):
        dest[i] = source[temp[i] - 1]
    return dest

def keyLeftMove(source, i):
    temp = 0
    global LS
    le = len(source)
    ls = LS[i]
    for k in range(ls):
        temp = source[0]
        for j in range(le - 1):
            source[j] = source[j + 1]
    source[le - 1] = temp
    return source

def keyPC_1(source):
    dest = [0] * 56
    temp = [57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]
    for i in range(56):
        dest[i] = source[temp[i] - 1]
    return dest

def diffOr(source1, source2):
    le = len(source1)
    dest = [0] * le
    for i in range(le):
        dest[i] = source1[i] ^ source2[i]
    return dest

def encryption(D, K):
    temp = [0] * 64;
    data = string2Binary(D)
    # 第一步初始置
    data = changeIP(data)
    left = [([0] * 32) for _ in range(17)]
    right = [([0] * 32) for _ in range(17)]
    for j in range(32):
        left[0][j] = data[j]
        right[0][j] = data[j + 32]
    setKey(K)  # sub key ok
    for i in range(1, 17):
        # 获取(48bit)的轮子密
        key = subKey[i - 1]
        # L1 = R0
        left[i] = right[i - 1]
        # R1 = L0 ^ f(R0,K1)
        fTemp = f(right[i - 1], key)  # 32bit
        right[i] = diffOr(left[i - 1], fTemp)
    # 组合的时候，左右调换
    for i in range(32):
        temp[i] = right[16][i]
        temp[32 + i] = left[16][i]

    temp = changeInverseIP(temp)
    str = binary2ASC(intArr2Str(temp))
    return str

def press(source):
    ret = [0] * 32
    temp = [([0] * 6) for i in range(8)]
    s = [s1, s1, s1, s1, s1, s1, s1, s1]
    st = []
    for i in range(8):
        for j in range(6):
            temp[i][j] = source[i * 6 + j]
    for i in range(8):
        x = temp[i][0] * 2 + temp[i][5]
        y = temp[i][1] * 8 + temp[i][2] * 4 + temp[i][3] * 2 + temp[i][4]
        val = s[i][x][y]
        ch = dec2hex(str(val))
        st.append(ch)
    ret = string2Binary(st)
    ret = dataP(ret)
    return ret

def dataP(source):
    dest = [0] * 32
    temp = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31,
            10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    le = len(source)
    for i in range(le):
        dest[i] = source[temp[i] - 1]
    return dest

def expend(source):
    ret = [0] * 48
    temp = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12,
            13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22,
            23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    for i in range(48):
        ret[i] = source[temp[i] - 1]
    return ret

def f(R, K):
    dest = [0] * 32
    temp = [0] * 48
    expendR = expend(R)
    temp = diffOr(expendR, K);
    dest = press(temp)
    return dest

def intArr2Str(arr):
    sb = []
    le = len(arr)
    for i in range(le):
        sb.append(str(arr[i]))
    return ''.join(sb)

def binary2ASC(s):
    st = ''
    ii = 0
    le = len(s)
    if le % 4 != 0:
        while ii < (4 - len % 4):
            s = "0" + s
    le = le / 4
    for i in range(int(le)):
        st += bin2hex(s[i * 4: i * 4 + 4])
    return st

D = '6666666666666666'
K = 'FFFFFFFFFFFFFFFF'

print(encryption(D,K))