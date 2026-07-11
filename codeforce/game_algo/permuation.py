M = 10**9


def solve(a: list[int]):
    hash0 = a[0]
    hash_win = a[0]
    _count = 0
    for i in range(1, len(a)):
        if hash0 < a[i] and a[i] > hash_win:
            hash_win = a[i]
            _count += 1
        hash0 = min(hash0, a[i])

    return _count


t = int(input())

for _ in range(t):
    _ = input()
    a = list(map(int, input().split()))
    print(solve(a))
