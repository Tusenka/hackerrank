t=int(input())


def solve(t, h, u):
    if t>u+2*h:
       return 2*t+2*u+3*h+1
    else:
      return 2*t+3*u-min(t,u)+3*h

for _ in range(t):
    t,h,u=tuple(map(int, input().split()))

    print(solve(t,h,u))