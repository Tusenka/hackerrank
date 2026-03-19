def solve(a: list):
    n = len(a)
    for i in range(n):
        if a[i] == n - i:
            continue
        j = i + 1
        while j < n and a[j] != n - i:
            j += 1
        a[i : j + 1] = list(reversed(a[i : j + 1]))
        break

    return a


t = int(input())
for _ in range(t):
    _ = input()
    a = list(map(int, input().split()))

    print(*solve(a))
