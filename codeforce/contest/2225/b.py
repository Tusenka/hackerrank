def solve(s: str ):
    h=set()
    for i in range(1, len(s)):
        h.add(i)

    if len(h)>2:
        return False

    return True

t=int(input())

for _ in range(t):
    s=input()

    print("YES" if solve(s) else "NO")