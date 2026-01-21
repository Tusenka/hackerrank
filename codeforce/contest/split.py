def solve(w, h, a):
    if w < h:
        w, h = h, w
    res1 = [x for x in a if x <= w]
    res2 = [x for x in a if x <= h]
    if len(res1) // 2 - len(res2) < 1:
        return len(res1) // 2

    return len(res2)


t = int(input())

for _ in range(t):
    n, w, h = tuple(map(int, input().split()))
    a = list(map(int, input().split()))

    print(solve(w, h, a))
