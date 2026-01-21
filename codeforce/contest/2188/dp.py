M=998244353

def solve(x: int, y: int, c: list[int]):
   # if x==y-1:
    #    assert False

    dp=[0 for _ in range(len(c)+1)]

    v=x+y
    for i in range(1,len(c)+1):
        if c[i-1]==1:
           dp[i]=(y-dp[i-1])%M
        elif c[i-1]==0:
            dp[i]=(x+dp[i-1]) % M
        else:
            dp[i]=v%M
            v*=2

    return sum(dp)%M

t=int(input())

for _ in range(t):
    n,x,y=tuple(map(int,input().split()))
    c=[1 if i=='1' else 0 if i=='0' else -1 for i in input()]

    print(solve(x=x,y=y, c=c))