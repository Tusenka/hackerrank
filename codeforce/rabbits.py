#https://codeforces.com/contest/2147/problem/C

def solve(a: str):
    dp=[[False for _ in range(3)] for _ in range(len(a))] # 0 full, 1 to left, 2 to right
    if a[0]=='0':
        dp[0][1]=True
        dp[0][2]=True
        dp[0][0]=True
    else:
        dp[0][1]=True
        dp[0][2]=False

    for i in range(1,len(a)):
        if a[i]=='1':
           dp[i][1]=dp[i-1][0] or dp[i-1][1]
           dp[i][2]=dp[i-1][2] and not a[i-1]=='1' and i<len(a)-1
           dp[i][0]=False

        else:
           dp[i][1]=dp[i-1][0] or dp[i-1][2]
           dp[i][2]=dp[i-1][1]

        if not any(dp[i]):
            return False

    return any(dp[-1])

t=int(input().rstrip())
for _ in range(t):
    _=input().rstrip()
    s=input().rstrip()
    print("YES" if solve(s) else "NO")


