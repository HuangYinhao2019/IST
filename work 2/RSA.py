import random
# 求乘法逆元
# 快速指数运算

p = 197
q = 173

n = p * q
fn = (p-1)*(q-1)

def qe(x,y,n): #x^y % n 快速指数运算 O(logn)
    s,t,u = 1,x,y
    while u:
        if u & 1:
            s = s * t % n
        u = u >> 1
        t = t * t % n
    return s

def MRprimeTest(p, t):  # 素数p，次数t
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

while True:
    publickey = random.randint(2,fn-1)
    if gcd(publickey,fn) == 1:
        break

privatekey,y = ex_eulid(publickey,fn)
privatekey %= fn

print("公钥为："+str(publickey)+",私钥为："+str(privatekey))
print(publickey*privatekey%fn)


text = random.randint(2,fn-1)
print("原文:",text)
code = qe(text,publickey,n)
print("加密后:",code)
decrypt = qe(code,privatekey,n)
print("解密后:",decrypt)
