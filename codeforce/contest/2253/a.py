
def solve(n: int):
    n=n+1
    for x in range(n-1, 1, -1):
        if not n%x:
            return False

    return True

t=int(input())

for _ in range(t):
    n=int(input())
    print("YES" if solve(n) else "NO")