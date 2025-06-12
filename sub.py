from functools import lru_cache, reduce
@lru_cache
def _gcd(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

def _gcd_array(a: list):
    return reduce(lambda v, e: _gcd(v, e), a, a[0])

def _gcd_array_add_e(a, gcd, e):
    return _gcd(gcd, a[e])

def _gcd_array_del_e(a, gcd, e):
    return _gcd_array(a)

def _iterate(n):
    x = 2 ** (n)
    for s in range(x):
        s = str(bin(s))[2:]
        s = s.zfill(n)
        yield s

def generate(a):
    for x in _iterate(len(a)):
        if x=='0'*len(a) or x=='1'*len(a):
            continue
        gcd1=_gcd_array([a[i] for i in range(len(a)) if x[i]=='1'])
        gcd2=_gcd_array([a[i] for i in range(len(a)) if x[i]=='0'])
        if gcd1!=gcd2:
           return True, [ int(v)+1 for v in x ]
    return False, []

if __name__ == '__main__':
    n = int(input().rstrip())
    for i in range(n):
        _=input()
        a = list([int(x) for x in input().rstrip().split()])
        res=generate(a)
        if res[0]:
            print("YES")
            print(*res[1])
        else:
            print("NO")

