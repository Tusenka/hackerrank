def solve(p: int, q: int):
    if q==0:
       if p<4:
           return None

       if (p-4)%3:
          return None

       return (p-4)//3

    if q==1:
        if p<3:
            return None

        if (p-2)%3:
            return None

        return (p-2)//3

    q-=2
    m=1

    while True:
        if q>0:
           q-=1

        else:
            if (p-2)%3:
                return None

            return (p-2)//3 + m



t=int(input())

for _ in range(t):
    p,q=tuple(map(int, input().split()))

    ans=solve(p, q)
    if ans:
        print(solve(p,q), 1)
    else:
        print(-1)
