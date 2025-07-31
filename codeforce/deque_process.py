# https://codeforces.com/contest/2128/problem/B


def solve(p: list,  q: list, res: list, l=0, r=-1, i=0, sign=0, longest=0):

    assert i<2 or q[i-1]!=q[i-2]
    longest, sign = get_longest(i, longest, q, sign)

    if longest>=4:
        return False
    if i==len(p)-1:
        q[i]=p[l]
        longest, _ = get_longest(i, longest, q, sign)
        return longest<4
    r=r if r>=0 else len(p)-1
    assert r>=l
    res[i]='L'
    q[i]=p[l]
    ltry=solve(p, q, res, l=l+1, r=r, i=i+1, sign=sign, longest=longest)
    if ltry:
        return q
    q[i] = p[r]
    res[i]='R'
    rtry = solve(p, q, res, l=l, r=r-1, i=i + 1, sign=sign, longest=longest)
    if rtry:
        return q
    return False


def get_longest(i, longest, q, sign):
    if i > 1 and q[i - 1] * sign < q[i - 2] * sign:
        longest += 1
    elif i > 1:
        sign = 1 if q[i - 1] < q[i - 2] else -1
        longest = 1
    else:
        longest = 0
    return longest, sign


t = int(input())

for i in range(t):
    n = tuple(int(x) for x in input().rstrip().split())
    p = list(int(x) for x in input().rstrip().split())
    res = ['L'] * len(p)
    q=[-1] * len(p)
    solve(p, q, res)
    print(''.join(res))
