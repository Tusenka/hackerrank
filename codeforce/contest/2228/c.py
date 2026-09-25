def solve(a: int, d: list[int]):
    h=[[-1, -1] for _ in range(10)]
    d=set(d)
    for i in range(10):
       if i in d:
          h[i]=[i,i]
          continue
       j=i
       while j>=0 and (j not in d):
           j-=1
       h[i][0]=j

       j=i
       while j<=9 and (j not in d):
            j+=1

       h[i][1]=j

    da=[int(x) for x in str(a)]
    up=False
    for i,x in enumerate(da):
        if x in d:
           continue

        up=h[x][1]<10 and (abs(h[x][1]-x)>abs(h[x][0]-x)) or h[x][0]<0
        break

    else:
        return 0

    res=[x for x in da]

    for i,x in enumerate(da):
        if up:
           if h[x][1]<10:
              res[i]=h[x][1]
           else:
              res[i]=h[x][0]
        else:
            if h[x][0]>-1:
                res[i]=h[x][0]
            else:
                res[i]=h[x][1]
    return min(abs(a-int(str(max(d))*(len(da)-1)) if len(da)>1 else 10**9), abs(a-int("".join(str(x) for x in res))))

t=int(input())

for _ in range(t):
    a,n = list(map(int, input().split()))
    d=list(map(int, input().split()))
    print(solve(a, d))