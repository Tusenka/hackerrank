def solve(a: int, b: int) -> tuple[int, list[int]]:
    x = a ^ b
    x = 1
    while x <= a:
        x = x << 1
    x -= 1
    if b > x:
        return -1, []
    x1 = a ^ x
    x2 = x ^ b

    return 2, [x1, x2]


t = int(input().rstrip())

for _ in range(t):
    a, b = tuple(map(int, input().strip().split()))
    res = solve(a, b)
    if res[0] > 0:
        print(res[0])
        print(*res[1])
    else:
        print(-1)
