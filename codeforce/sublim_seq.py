def solve(x, n):
    if n % 2 == 0:
        return 0
    else:
        return x


t = int(input().rstrip())

for _ in range(t):
    x, n = tuple(map(int, input().rstrip().split()))
    print(solve(x, n))
