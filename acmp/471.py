def transitions(n):
    t={1: [6, 8], 2: [9, 7], 3: [4,8], 4: [3, 0, 9], 5:[], 6: [1, 7, 0], 7: [2, 6], 8: [1,3], 9: [2, 4] ,0: [4, 6]}

    return t[n]

def solve(n):
    dp=[[1 for _ in range(10)] for _ in range(n+1)]


    for i in range(n):
        dp[1][i]=1

    for s in range(2, n+1):
        for i in range(10):
            dp[s][i]=sum(dp[s-1][j] for j in transitions(i)) if transitions(i) else 0

    return sum(dp[n][1:8]+[dp[n][9]])


n=int(input())

print(solve(n))