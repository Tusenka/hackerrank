def dfs(i: int, a: list, visited=None, res=None) -> list[int]:
    if res is None:
        res = []
    if visited is None:
        visited = set()

    visited.add(i)

    for j in a[i]:
        if j not in visited:
            visited.add(j)
            dfs(i=j, a=a, visited=visited, res=res)

    res.append(i)

    return res


def sort(at: list) -> list[int]:
    visited = set()
    res = []

    for i in range(len(at)):
        if i not in visited:
            dfs(i=i, a=at, visited=visited, res=res)

    return list(reversed(res))


def solve(a: list, at: list) -> tuple[int, list[int]]:
    touts = sort(at)

    result = [-1] * len(a)
    ii = 1

    for i in touts:
        if result[i] >= 0:
            continue
        res = dfs(i=i, a=a)

        for j in res:
            if result[j] >= 0:
                continue
            result[j] = ii

        ii += 1

    for i in range(len(result)):
        result[i] = ii - result[i]

    return ii - 1, result


n, m = tuple(map(int, input().rstrip().split()))

a = [set() for _ in range(n)]
at = [set() for _ in range(n)]

for _ in range(m):
    i, j = list(map(int, input().rstrip().split()))
    a[i - 1].add(j - 1)
    at[j - 1].add(i - 1)

res = solve(a=a, at=at)

print(res[0])
print(*res[1])
