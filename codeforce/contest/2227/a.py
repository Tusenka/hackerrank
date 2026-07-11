def solve(x,y):
    return not x%2 or not y%2

t=int(input())

for _ in range(t):
    x,y=tuple(map(int, input().split()))

    print("YES" if solve(x,y) else "NO")