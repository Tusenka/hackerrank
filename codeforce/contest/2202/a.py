def solve(x,y):
    if y*2>x:
        return False
    if y>=0:
       rest=x-2*y
       if not rest or rest%3==0:
          return True
       return False
    if y<0:
       rest=x+4*y
       if rest<0:
           return False

       if not rest or rest%3==0:
           return True
       return False


t=int(input())

for _ in range(t):
    x, y = tuple(map(int, input().split()))
    print("YES" if solve(x,y) else "NO")