#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=15&id_topic=15&id_problem=1105
M=(10**9)

def solve(a: list):
    a.sort()
    # a - [(age, risk)]
    dp=[[0 for _ in range(2)] for _ in range(len(a))]
    dp[0][0]=0
    dp[0][1]=M

    for i in range(1, len(a)):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = min(dp[i-1][0] + a[i][1], dp[i-1][1]+a[i][1])

    return dp[-1][1]

t = int(input())

raw = list(map(int, input().split()))

a=[(0 for _ in range(2)) for _ in range(t)]

for i in range(0, len(raw)-1, 2):
    a[i//2]=(raw[i], raw[i+1])

print(solve(a=a))
