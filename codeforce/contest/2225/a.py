def solve(x: int, y: int):

    if y%(x+1):
        return "YES"
    else:
        return "NO"

t=int(input())

for _ in range(t):
    x,y=tuple(map(int, input().split()))
    print(solve(x,y))
