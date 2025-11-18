# https://codeforces.com/contest/2127/problem/A
M = 200


def mex(a, b, c):
    _min = min(a, b, c)
    if _min > 1:
        return _min - 1
    aa = sorted([a, b, c])

    if aa[0] + 1 >= aa[1] and aa[1] + 1 >= aa[2]:
        return aa[2] + 1

    if aa[0] + 1 < aa[1]:
        return aa[0] + 1
    else:
        return aa[1] + 1


def try_mex(a, i):
    x = len([1 for x in a[i : i + 3] if x == M])

    if x >= 3:
        return True

    if x == 2:
        return 0 in a[i : i + 2]

    _min = min(a[i : i + 3])
    _max = max([x for x in a[i : i + 3] if x != M])

    if x == 1:
        diff = mex(a[i], a[i + 1], a[i + 2])

        if _max - _min > diff:
            return False

        else:
            iM = [j for j in range(i, i + 3) if a[j] == M][0]
            a[iM] = _min + diff
            return True

    if x == 0:
        return mex(a[i], a[i + 1], a[i + 2]) == _max - _min


t = int(input().rstrip())


def solve(a):
    return all(try_mex(a, i) for i in range(len(a) - 2))


for _ in range(t):
    _ = int(input().rstrip())
    a = list(int(x) if x != "-1" else M for x in input().rstrip().split())
    print("YES" if solve(a) else "NO")
