# https://codeforces.com/contest/2136/problem/A
def solve(x, y):
    if x > y:
        x, y = y, x
    l = x + y

    if x == 0 and y == 0:
        return True

    if l // 3 <= x:
        return True

    if l < 3:
        return True

    return False


t = int(input().rstrip())

for _ in range(t):
    a1, b1, a2, b2 = tuple(map(int, input().rstrip().split()))
    print("YES" if solve(a1, b1) and solve(a2 - a1, b2 - b1) else "NO")
