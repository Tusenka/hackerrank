from functools import cache

_seq = []
_dp = {}


def _build_seq(seq, r):
    n = len(seq)
    if r <= n:
        return seq
    _count = 0
    _counts = [0] * ((r + 1) // 2)
    for i in range(n):
        if seq[i] == 1:
            _count += 1
        _counts[i] = _count % 2
    return _counts


def _get_value(_counts: list, r: int):
    n = len(_counts)
    if (r + 1 // 2 - 1) <= n:
        return _counts[(r + 1) // 2 - 1]
    _count = _get_value(_counts, (r + 1) // 2 - 1)
    if _count % 2 == 1:
        return _count+1
    else:
        return _count


if __name__ == '__main__':
    t = int(input().rstrip())
    for t_itr in range(t):
        (n, l, r) = tuple([int(x) for x in input().rstrip().split()])
        a = list([int(x) for x in input().rstrip().split()])
        print(_get_value(_build_seq(a, r), r) %2==0)
