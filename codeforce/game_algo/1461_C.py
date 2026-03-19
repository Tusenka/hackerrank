from typing import NamedTuple


class Op(NamedTuple):
    end: int
    p: float


def solve(a: list[int], ops: list[Op]):
    _a = sorted(a)
    _last = 0
    for j in range(len(_a), -1, -1):
        if a[j] != _a[j]:
            _last = j

    ans = sum([o.p for o in ops if o.end >= _last])
    return ans


for _ in range(int(input())):
    n, m = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    ops = []
    for i in range(m):
        e, p = tuple(map(int, input().split()))
        ops.append(Op(e, p))
    print(solve(a, ops))
