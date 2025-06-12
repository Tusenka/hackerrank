#https://codeforces.com/problemset/problem/1516/B
from functools import reduce

dp=[]
def _xor(a: list[int]):
    return reduce(lambda x, y: x^y, a)

def _eval(a: list):
    _prefix =[0]*len(a)
    _suffix=[0]*len(a)
    _prefix[0]=a[0]
    _suffix[-1]=a[-1]
    for i in range(1, len(a)):
        _prefix[i]=a[i]^_prefix[i-1]
    for i in range(len(a)-2, -1, -1):
        _suffix[i]=a[i]^_suffix[i+1]
    for  i in range(len(a)-1):
        if _suffix[i+1]==_prefix[i]:
            return True
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if _suffix[j]==_prefix[i] and _xor(a[i+1:j])==_suffix[j]:
                return True
    return False
t=int(input())
for _ in range(t):
    _=input()
    s=[int(x) for x in input().split()]
    print("YES" if _eval(s) else "NO")