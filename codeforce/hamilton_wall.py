#https://codeforces.com/problemset/problem/1766/C?locale=en
import math


def check_bit(i, j):
    return i & (1<<j)

def _hash(i, j, m):
    return i*m+j

def _dehash(v, m):
    return v//m, v%m

def solve(s):
    m=len(s[0])
    dp=[[False for _ in range (m*2)] for _ in range (1<<(m*2))]
    last=0
    last_mask=0
    for i in range(2*m):
        i0, i1 = _dehash(i, m)
        if s[i0][i1] == 'B':
            last = i
            last_mask = last_mask ^ (1<<i)
            dp[1 << i][i] = True
    for mask in range(2, 1<<(m*2)):
        for ii in range(last):
            i0, i1 = _dehash(ii, m)
            if not check_bit(mask, ii) or s[i0][i1]=='W' or not dp[mask][ii]:
                continue
            steps=[]
            if i0==0:
                steps.append((i0+1, i1))
            else:
                steps.append((i0-1, i1))
            if i1<m-1:
                steps.append((i0, i1+1))
            if i1>0:
                steps.append((i0, i1-1))
            for step in steps:
                k0, k1 = step
                kk=_hash(k0, k1, m)
                if check_bit(mask, kk) or s[k0][k1]=='W':
                    continue
                dp[mask^(1<<kk)][kk]=True

    return dp[last_mask][last]


t=int(input())

for _ in range(t):
    _ = input().rstrip()
    s=['']*2
    s[0]=input().rstrip()
    s[1]=input().rstrip()
    if solve(s):
        print("YES")
    else:
        print("NO")

