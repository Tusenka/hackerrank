def solve(x: int, y: int):
    return x>=y and x%y==0


t=int(input())

for _ in range(t):
    x,y=tuple(map(int, input().split()))
    print("YES" if solve(x,y) else "NO")