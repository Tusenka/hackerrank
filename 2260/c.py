def solve(x: int,y:int):
    s=x+y
    count=0
    for i in range(29,-1,-1):
        if s&(1<<i)==0:
            continue
        if s>(1<<i):
            count+=1<<i

    return s,count
t=int(input())

for _ in range(t):
    x,y=tuple(map(int, input().split()))

    print(*solve(x,y))