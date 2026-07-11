def solve(k: int, a: list[int]):
    a.sort()
    ki=[]
    ik={}
    _x=k
    _i=0

    for x in a:
        if x>1 and x%k:
            return False

    ki.append(1)
    while _x<a[-1]*k:
        ki.append(_x)
        ik[_x]=_i
        _x*=k

    for i in range(len(ki)-1,-1,-1):
        _c=0
        _j=None
        for j,x in enumerate(a):
            if x>=ki[i]:
               _c+=1
               _j=j
            if _c>1:
                return False

        if _j is not None:
            a[_j]-=ki[i]

    return True




t=int(input())

for _ in range(t):
    n, k = tuple(map(int, input().split()))
    a = list(map(int, input().split()))

    print("YES" if solve(k=k, a=a) else "NO")
