
def _mex(a: list, n):
    _h=[0]*(n+1)
    for x in a:
       _h[x]=1

    return min(i for i in range(n+1) if _h[i]==0)

def solve(a: list[int]):
    dp=[[-1 for _ in range(len(a))] for _ in range(len(a))]

    for i in range(len(a)):
        dp[i][i]=a[i]-1 if a[i] else 1

    for i in range(len(a)-1):
        if a[i]==a[i+1]:
           dp[i][i+1]=a[i]-1 if a[i] else 1

    for k in range(3, len(a)+1):
        for i in range(len(a) - k + 1):
            j = i + k - 1

            if dp[i + 1][j - 1]>=0 and a[i] == a[j]:
               if dp[i+1][j-1]==a[i]:
                  dp[i][j]=_mex(a[i:j+1], len(a)//2)
               else:
                  dp[i][j]=dp[i+1][j-1]


    return max(max(x) for x in dp)

t=int(input())

for _ in range(t):
    input()
    a=list(map(int, input().split()))

    print(solve(a))