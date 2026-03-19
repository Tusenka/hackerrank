from math import sqrt


def solve(a: list[int]):
    n = len(a)
    ans = 0
    for x in range(int(sqrt(n))):
        for j in range(n):
            i = j - x * a[j]
            if i >= 0 and a[i] == x:
                ans += 1
            # i=j+x*a[j]
            # if i<n and a[i]==x:
            #     ans+=1
    return ans

    for i, x in enumerate(a):
        _step = 1
        for j in range(i + x, len(a), x):
            if a[j] == _step:
                ans += 1
            _step += 1
    return ans


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print(solve(a=a))
