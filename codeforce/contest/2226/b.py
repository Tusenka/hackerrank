import math

M = 10**9

def load(
        a: list, i=0, begin=0, end=-1, result: list[list[int]] | None = None
) -> list[list[int]]:
    n = (len(a)) * 4
    end = len(a) - 1 if end == -1 else end

    if result is None:
        result = [[-1, M, a[begin]] for _ in range(n)]

    if begin == end:
        result[i] =[a[begin], a[begin], a[begin]]

        return result

    l = i * 2 + 1
    r = i * 2 + 2
    m = (begin + end) // 2
    load(a, l, begin, m, result=result)
    load(a, r, m + 1, end, result=result)

    result[i] = [max(result[l][0], result[r][0]), min(result[l][1], result[r][1]), math.gcd(result[l][2], result[r][2])]

    if i == 0:
        return result

    return []


def _get_value(res: list[list[int]], l: int, r: int, idx: int, begin: int, end: int):
    if begin > r or end < l:
        return [-1, M, 1]

    if begin == end:
        return res[idx]

    if begin == l and r == end:
        return res[idx]

    m = (begin + end) // 2

    r1=_get_value(res=res, l=l, r=r, idx=idx * 2 + 1, begin=begin, end=m)
    r2=_get_value(res, l, r, idx * 2 + 2, m + 1, end)

    return [max(r1[0], r2[0]), min(r1[1], r2[1]), math.gcd(r1[2],r2[2])]


def get_value(res: list[list[int]], l: int, r: int):
    return _get_value(res=res, l=l, r=r, idx=0, begin=0, end=len(res) // 4 - 1)


def solve(a: list):
    res = load(a)

    ans=0

    for i in range(len(a)):
        for j in range(i+1, len(a),1):
            v=get_value(res=res, l=i, r=j)

            if v[0]-v[1]==v[2]:
                ans+=1

    return ans


t=int(input())

for _ in range(t):
    input()

    a=list(map(int, input().split()))
    print(solve(a))
