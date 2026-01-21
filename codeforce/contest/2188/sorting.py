M=10*9
def solve(a:list)->int:
    asort=sorted(a)
    if a==asort:
        return -1
    d=[max(a[i]-asort[0], asort[-1]-a[i]) if a[i]!=asort[i] else M for i in range(0, len(a))]
    return min(d)

t=int(input())

for _ in range(t):
    _=input()
    a=list(map(int, input().split()))
    print(solve(a))
