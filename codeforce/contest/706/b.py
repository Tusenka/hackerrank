def bin_search(r, f):
    l = 0
    while l < r:
        mid = (l + r) // 2
        if f(mid):
            r = mid
        else:
            l = mid + 1

    return l


def solve(x:list[int], m:list[int]):
    ans=[0]*len(m)
    x.sort()

    for v in m:
        c=


_ =input()
x=list(map(int,input().split()))
t=int(input())
m=[0]*t

for i in range(t):
    m[i]=int(input())
