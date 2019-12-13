import random
# 求乘法逆元
# 快速指数运算

def qe(x,y,n): #x^y % n 快速指数运算 O(logn)
    s,t,u = 1,x,y
    while u:
        if u & 1:
            s = s * t % n
        u = u >> 1
        t = t * t % n
    return s

def MRprimeTest(p, t):  # 素数p，次数t, 素性检测
    q = p - 1
    k = 0
    while q & 1 == 0:
        q >>= 1
        k += 1
    for i in range(t):
        r = random.randint(2,p-2)
        x = qe(r,q,p)
        for j in range(k): #k次二次探测法
            nx = qe(x,2,p)
            if nx == 1 and x != 1 and x != p - 1:
                return False
            x = nx
        if x != 1:
            return False
    return True

def gcd(a,b):  #最大公约数
    while a % b != 0:
        r = a % b
        a = b
        b = r
    return b

def ex_eulid(a,b):  #拓展欧几里得求逆元
    if b == 0:
        return 1,0
    else:
        k = a // b
        r = a % b
        x1,y1 = ex_eulid(b,r)
        x ,y = y1,x1-k*y1
    return x,y

if __name__ == "__main__":
    while True:
        print("输入素数 p:")
        p = int(input())
        if MRprimeTest(p,20):
            break
    while True:
        print("输入素数 q:")
        q = int(input())
        if MRprimeTest(q, 20):
            break

    n = p * q
    fn = (p - 1) * (q - 1)

    while True:
        publickey = random.randint(2, fn - 1)
        if gcd(publickey, fn) == 1:
            break

    privatekey, y = ex_eulid(publickey, fn)
    privatekey %= fn

    print("公钥为e：" + str(publickey) + " n:",n)
    print("私钥为d：" + str(privatekey) + " n:",n)
    print("验证publickey * privatekey % fn =",publickey * privatekey % fn)

    print("输入原文(<fn:"+str(fn)+"):")
    text = int(input())
    print("原文:",text)
    code = qe(text,publickey,n)
    print("加密后:",code)
    decrypt = qe(code,privatekey,n)
    print("解密后:",decrypt)
