def score(a: list, b: list, x: int):
    j = 0
    n = 0
    i = 0
    last = 0
    while i < len(a) and j < len(b):
        if b[j] < x:
            j += 1
            continue

        if a[i] <= b[j] + last:
            j += 1
            i += 1
            n += 1
        else:
            last += b[j]
            j += 1

    return n * x


def solve(a, b):
    c = sorted(b)
    last = score(a, b, c[0])
    start = last
    l = 0
    r = len(c) - 1
    dir = 1
    while r > l:
        mid = (l + r) // 2
        current = score(a, b, c[mid])
        if current > last:
            if dir == 1:
                l = mid
            else:
                r = mid
        else:
            if dir == 1:
                r = mid
            else:
                l = mid
            dir *= -1

        last = current

    return max(last, start)


t = int(input())

for _ in range(t):
    n = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(solve(a, b))
