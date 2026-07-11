def solve(a):
    a = [(a[i], i % 2) for i in range(len(a))]
    a.sort()
    for i in range(1, len(a)):
        if a[i][1] == a[i - 1][1]:
            return False

    return True


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print("YES" if solve(a) else "NO")
