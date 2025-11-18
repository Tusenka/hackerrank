def solve(a: list[int]):
    return [i+1 for i in range(len(a)) if a[i]==0]


t = int(input().rstrip())

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().rstrip()))
    res=solve(a)
    print(len(res))
    print(*res)


