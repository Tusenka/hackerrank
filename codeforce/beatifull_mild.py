def solve(a: list[int]):
    mild=0
    cur=0
    return max(a)
        for r in range(l+1, len(a)):
            cur+=a[r]
            cur=cur*(r-l-1)/(r-l)
            if cur>mild:
                mild=cur

    return cur


def solve(a: list())

t = int(input().rstrip())

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    print(solve(a))

