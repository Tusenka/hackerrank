def solve(a):
    dp = []
    pass


t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    a = list(map(int, input().rstrip().split()))
    print(solve(a))
