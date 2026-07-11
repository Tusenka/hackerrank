def solve(a: list[int]):
    a.sort(reverse=True)
    last=-1
    for x in a:
        if x==last:
           return [-1]
        last=x

    return a

t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))

    print(*solve(a=a))