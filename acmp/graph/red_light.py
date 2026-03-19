def check_loop(i: int, j: int, k: int, p: tuple, d: tuple):
    diff = p[i] - p[j]
    pass


def solve(k: int, p: tuple, d: tuple, x: int):
    pass


t = int(input().strip())
for i in range(t):
    n, k = tuple(map(int, input().split()))
    p = tuple(map(int, input().split()))
    d = tuple(map(int, input().split()))

    q = int(input().strip())

    for _ in range(q):
        x = int(input().strip())
        print(solve(k=k, p=p, d=d, x=x))
