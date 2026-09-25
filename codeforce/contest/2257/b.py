def solve(a:list[int],b:list[int]):
    xa=a[0]+len(a)-1
    xb=b[0]+len(b)-1

    if xa>=xb:
        return 1
    else:
        return 2


t=int(input())

for _ in range(t):
    input()
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))

    print(solve(a=a, b=b))