def solve(x:int, y:int, a:list):
    _count=sum([(v//x) for v in a])
    dp=[0]*len(a)
    for i,v in enumerate(a):
        dp[i]=y*(_count-v//x)+a[i]
    return max(dp)

t= int(input())

for _ in range(t):
    n, x,y=tuple(map(int, input().split()))

    a=list(map(int, input().split()))
    print(solve(x=x, y=y, a=a))