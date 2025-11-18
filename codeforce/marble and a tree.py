#https://codeforces.com/problemset/problem/2138/C1?locale=en

def solve(a, i, depth, leafs):
    depth+=1

    for i,d in enumerate(depth):
        if not leafs[i]:
            continue
    depth=min(d for i,d in enumerate(depth) if leafs[i])


def _dfs(a: list, i: int, depth: list, leafs: list):
    if a[i]==-1:
        return
    if depth[i]>0:
        return

    leafs[a[i]] = False
    _dfs(a=a, i=a[i], depth=depth, leafs=leafs)
    depth[i]=depth[a[i]]+1
    return

t=int(input())

for i in range(t):
    _,k=tuple(map(int,input().split()))
    a=[-1]+[int(i)-1 for i in input().split()]

    depth=[0]*len(a)
    leafs=[True]*len(a)
    leafs[0]=False

    for i in range(1,len(a)):
        _dfs(a=a, i=i, leafs=leafs, depth=depth)

    print(*depth)
    print(*leafs)
    solve(a, k)
