def solve(a: list[int], m:int, k:int):
    l=0
    r=len(a)-1

    ans=0
    ls=0
    rs=0
    while l<r:
        if a[l]==1:
            l+=1
            ls=0
        elif a[l]==0:
           ls+=1
           if ls>=m:
              l+=k
              ls=0
              ans+=1
           else:
               l+=1
        if a[r]==1:
            r-=1
            rs=0
        elif a[r]==0 and l<r:
            rs+=1
            if rs>=m:
                r-=k
                rs=0
                ans+=1
            else:
                r-=1

    return ans

t=int(input())

for _ in range(t):
    n,m,k=tuple(map(int, input().split()))
    a=list(map(int, input()))
    print(solve(a=a,m=m,k=k))
