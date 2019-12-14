def get_inverse_element(value, max_value):
    for i in range(1, max_value):
        if (i * value) % max_value == 1:
            return i
    return -1

def gcd_x_y(x, y):
    if y == 0:
        return x
    else:
        return gcd_x_y(y, x % y)

def calculate_p_q(x1, y1, x2, y2, a, p):
    flag = 1  # 定义符号位
    if x1 == x2 and y1 == y2:
        member = 3 * (x1 ** 2) + a  # 计算分子
        denominator = 2 * y1  # 计算分母
    else:
        member = y2 - y1
        denominator = x2 - x1
        if member * denominator < 0:
            flag = 0
            member = abs(member)
            denominator = abs(denominator)

    # 将分子和分母化为最简
    gcd_value = gcd_x_y(member, denominator)
    member = int(member / gcd_value)
    denominator = int(denominator / gcd_value)
    # 求分母的逆元
    inverse_value = get_inverse_element(denominator, p)
    k = (member * inverse_value)
    if flag == 0:
        k = -k
    k = k % p
    # 计算x3,y3
    x3 = (k ** 2 - x1 - x2) % p
    y3 = (k * (x1 - x3) - y1) % p
    # print("%d<=====>%d" % (x3, y3))
    return [x3, y3]

def get_order(x0, y0, a, p):
    # 计算-p
    x1 = x0
    y1 = (-1 * y0) % p
    temp_x = x0
    temp_y = y0
    n = 1
    while True:
        n += 1
        p_value = calculate_p_q(temp_x, temp_y, x0, y0, a, p)
        if p_value[0] == x1 and p_value[1] == y1:
            return n + 1

        temp_x = p_value[0]
        temp_y = p_value[1]

    # print("%d-%d-%d-%d" % (x0,y0,x1,y1))

def get_x0_y0_x1_y1(x0, a, b, p):
    y0 = -1
    for i in range(0, p):
        if i ** 2 % p == (x0 ** 3 + a * x0 + b) % p:
            y0 = i
            break

    # 如果y0找不到则返回False
    if y0 == -1:
        return False
    # 计算-y
    x1 = x0
    y1 = -1 * y0 % p
    # print("%d-%d-%d-%d" % (x0,y0,x1,y1))
    return [x0, y0, x1, y1]

def calculate_np(G_x, G_y, private_key, a, p):
    temp_x = G_x
    temp_y = G_y
    while private_key != 1:
        p_value = calculate_p_q(temp_x, temp_y, G_x, G_y, a, p)
        temp_x = p_value[0]
        temp_y = p_value[1]
        private_key -= 1
    return p_value

def m2point(m,a,b,k):
    for j in range(k):
        x = k * m + j
        y2 = (x * x * x + (a * x) + b) % p
        sy = int(y2 ** 0.5)
        if y2 / sy == sy:
            return [x,y2/sy]

if __name__ == '__main__':
    while True:
        a = int(input("请输入椭圆曲线的参数a:"))
        b = int(input("请输入椭圆曲线的参数b:"))
        p = int(input("请输入椭圆曲线的参数p(p为质数):"))

        if (4 * (a ** 3) + 27 * (b ** 2)) % p == 0:
            print("选取的椭圆曲线不能用于加密，请重新选择\n")
        else:
            break
    for i in range(1,p):
        value = get_x0_y0_x1_y1(i, a, b, p)
        if value != False:
            x0 = value[0]
            y0 = value[1]
            break
    print("选出一个点作为生成元G(%d,%d):" % (x0,y0))
    G_x = int(input("你选取的横坐标G_x:"))
    G_y = int(input("你选取的纵坐标G_y:"))
    n = get_order(G_x, G_y, a, p)
    private_key = int(input("输入私钥key(<%d):" % n))
    # 计算公钥 nG
    Pa = calculate_np(G_x, G_y, private_key, a, p)
    print("公钥为(%d,%d)" % (Pa[0],Pa[1]))
    # 加密开始
    k = int(input("请给出整数k(<%d):" % n))
    k_G = calculate_np(G_x, G_y, k, a, p)  # 计算kG
    k_Pa = calculate_np(Pa[0], Pa[1], k, a, p)  # 计算kPa
    m = int(input("请输入要加密的明文m："))
    [pm_x,pm_y] = m2point(m,a,b,30)
    print("m映射到椭圆曲线上点(%d,%d)" % (pm_x,pm_y))
    # pm_x = int(input("请输入要加密的明文点Pm横坐标x："))
    # pm_y = int(input("请输入要加密的明文点Pm纵坐标y："))
    [cx,cy] = calculate_p_q(pm_x,pm_y,k_Pa[0],k_Pa[1],a,p)
    # 密文为

    C = [k_G[0], k_G[1], cx, cy]
    print("密文为：{(%d,%d),(%d,%d)}" % (C[0], C[1], C[2], C[3]))
