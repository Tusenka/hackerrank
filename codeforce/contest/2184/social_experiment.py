def solve(n: int) -> int:
    if n < 3:
        return 2
    if n == 3:
        return 3

    return n % 2


t = int(input())

for _ in range(t):
    n = int(input())
    print(solve(n))
