def solve(n, a, b):
    if b % 2 != n % 2:
        return False
    if b >= a:
        return True
    if a % 2 != n % 2:
        return False

    return True


t = int(input().rstrip())

for _ in range(t):
    n, a, b = tuple(map(int, input().rstrip().split()))
    print("YES" if solve(n, a, b) else "NO")
