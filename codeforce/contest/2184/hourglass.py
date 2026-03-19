def solve(s: int, k: int, m: int):
    if k > s:
        return 0

    count = m // k
    if count % 2:
        rest = k
    else:
        rest = s

    if m % k:
        if m % k > rest:
            rest = 0
        else:
            rest = rest - m % k

    return rest


t = int(input())

for _ in range(t):
    s, k, m = tuple(map(int, input().split()))
    print(solve(s=s, k=k, m=m))
