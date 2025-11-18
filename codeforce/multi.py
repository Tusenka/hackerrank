#https://codeforces.com/contest/2147/problem/B
M=10**9

def solve(n: int):
    a=[-1]*2*n
    a[0]=n
    a[n]=n
    for i in range(1, n):
        a[i]=n-i
        a[-i]=n-i
    return a

m=int(input())
for _ in range(m):
    n=int(input())
    print(*solve(n))

