def solve(a: list)->int:
    return len(set(a))

t = int(input().rstrip())

for _ in range(t):
    _ = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    print(solve(a))

