def solve(a: list[int],b :list[int], k:int):
    n=len(a)
    check=set(a)
    for x in b:
        if x<0:
           continue
        if x not in check:
           return False

        check.remove(x)

    if k>=n:
        return True

    for i in range(n-k):
        if b[i]==-1:
            continue
        if a[i]!=b[i]:
           return False

    for i in range(n-1, n-k, -1):
        if b[i]==-1:
            continue

        if a[i]!=b[i]:
            return False

    return True

t=int(input())

for _ in range(t):
    n,k=tuple(map(int,input().split()))
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))

    print("YES" if solve(a=a, b=b, k=k) else "NO")
