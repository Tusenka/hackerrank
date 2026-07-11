# https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=32&id_topic=56&id_problem=1046
from math import ceil


def check(a):
    odd = 0
    for x in a:
        if len(x) % 2 != 0:
            odd += 1
        if odd > 2:
            return False, []
    return True


def solve(a, c, visited, i=0, output=None):
    if output is None:
        output = []
    for x in c[i]:
        ii, jj = x[1], x[2]
        if not visited[ii]:
            visited[ii] = True
            visited[jj] = True
            print(x[0])
            solve(a=a, c=c, visited=visited, i=x[0], output=output)
            output.append(jj + 1)
            output.append(ii + 1)
    return output


t = int(input().rstrip())
a = [-1 for _ in range(4 * t)]
c = [set() for _ in range(t)]
visited = [False for _ in range(4 * t)]

for _ in range(2 * t):
    ii, jj = tuple(map(int, input().rstrip().split()))
    a[ii - 1] = jj - 1
    a[jj - 1] = ii - 1
    c[ceil(ii / 4) - 1].add((ceil(jj / 4) - 1, ii - 1, jj - 1))
    c[ceil(jj / 4) - 1].add((ceil(ii / 4) - 1, jj - 1, ii - 1))


if not check(c):
    print("No")

else:
    print("Yes")
    ans = solve(a=a, visited=visited, c=c)
    print(*reversed(ans))
