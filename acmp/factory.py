# https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=21&id_topic=50&id_problem=646


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


def solve(a: list, p: list) -> tuple[int, list[int]]:
    result = dfs(0, a)
    return sum([p[i] for i in result]), result


n = int(input())
a = [set() for _ in range(n)]
p = list(map(int, input().rstrip().split()))

for i in range(n):
    c = list(map(int, input().rstrip().split()))
    for j in c[1:]:
        a[i].add(j - 1)

res = solve(a, p)
print(res[0], len(res[1]))
print(*[i + 1 for i in res[1]])
