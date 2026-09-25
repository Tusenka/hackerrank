
def solve(a: list[int]):
    p=[a[0]]*len(a)
    s=a[0]
    for i in range(1, len(a)):
        s+=a[i]
        p[i]=s//(i+1)

    pm=[a[0]]*len(a)
    for i in range(1, len(a)):
        pm[i]=min(p[i], pm[i-1])

    return pm

t=int(input())

for _ in range(t):
    input()
    a=list(map(int, input().split()))

    print(*solve(a=a))