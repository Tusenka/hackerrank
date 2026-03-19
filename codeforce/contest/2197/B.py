def solve(a: list, p: list):
    i = 0
    last = a[0]
    while i < len(a):
        if a[i] != p[i]:
            if i > 0 and (p[i - 1] == a[i] or last == a[i]):
                last = p[i - 1]
                i += 1
                continue
            j = i
            while j < len(a):
                if p[j] == a[i]:
                    i = j
                    break
                if j < len(a) - 1 and a[i] != a[j]:
                    return False
                j += 1
            else:
                return False
        i += 1
    return True


t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print("YES" if solve(a=b, p=p) else "NO")
