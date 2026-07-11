
def solve(a: list[int], d: int):
    cur=1
    ans=[cur]*len(a)
    x=[(a[i], i) for i in range(len(a))]
    x.sort()
    l=0
    h=[cur]*len(a)
    for i in range(1, len(a)):
        if x[i][0]-x[i-1][0]>d:
            l=i
        else:
            if i-l<cur:
                cur=1
            else:
                while x[i][0]-x[l][0]<=d and i-l>=cur and i>l:
                    l+=1
                    cur+=1
        h[i]=cur
        ans[x[i][1]]=cur


    return max(ans), ans



n,d=tuple(map(int, input().split()))
a=list(map(int, input().split()))

ans=solve(a=a, d=d)
print(ans[0])
print(*ans[1])