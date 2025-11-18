def solve(a: list, b: list):
    ans = 1
    for i in range(len(a)):
        if a[i] > b[i]:
            ans += a[i] - b[i]
    return ans


t = int(input().rstrip())

for _ in range(t):
    _ = int(input().rstrip())
    a = list(int(x) for x in input().rstrip().split())
    b = list(int(x) for x in input().rstrip().split())
    print(solve(a, b))
