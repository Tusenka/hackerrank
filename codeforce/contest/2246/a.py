def solve(n: int):
    return [i for i in range(n, 0, -1)]

t=int(input())

for i in range(t):
    n=int(input())

    print(*solve(n))

