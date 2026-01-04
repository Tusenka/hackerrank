from copy import copy


def solve(a:list[int],m:int):
    n=len(a)
    a=[(a[i], i) for i in range(n)]
    a.sort()

    if m*2>n:
        return -1
    if m==0:
       h=copy(a)
       l,r=0, len(h)-1
       r1=len(h)-1
       ans=[]

       while l<r:
           val=a[r][0]
           for i in range(l, r):
               val-=a[i][0]
               ans.append((a[i][1], a[r][1]))
               if val<=0:
                   l=i
                   r-=1
                   break
           else:
               return -1

       return ans

    ans=[]
    x=n-m*2

    for i in range(x):
        ans.append((a[i+x][1], a[i][1]))

    for i in range(0, m):
        ans.append((a[i+x][1], a[i+x+m][1]))

    return ans


t=int(input())
for _ in range(t):
    n, m= tuple(map(int, input().split()))
    a=list(map(int, input().split()))
    ans=solve(a=a, m=m)
    if ans==-1:
        print(-1)
    else:
        print(len(ans))
        for x in ans:
            print(x[0]+1, x[1]+1)