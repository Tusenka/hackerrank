def solve(x: list[int]):
    x = [x[0]] + sorted(x[1:])

    _sum = x[0]
    for i in range(1, len(x)):
        if _sum + x[i] > 9:
            return len(x) - i
        _sum += x[i]

    return 0


t = int(input())

for _ in range(t):
    x = [int(x) for x in input()]
    print(solve(x))
