def _for_exists():
    pass

def _iterate_cut(a:tuple, l, r):
    for i in range(l, r-1):
        for j in range(i+1, r):
            for k in range(r, i, -1):
                yield a[i]*a[j]*a[k], (l, i), (k, r)


def _triangle(a):
    _dp=[[ 0 for _ in range(len(a))] for _ in range(len(a))]
    for k in range(3, len(a)):
        for i in range(len(a)-k):
            _max=0
            for _cut in _iterate_cut(a, i, i+k):
                _cost=_cut[0]+_dp[_cut[1][0]][_cut[1][1]]+_dp[_cut[2][0]][_cut[2][1]]
                if _cost>_max:
                   _max=_cost
            _dp[i][i+k]=_max
    return _dp[0][-1]



q = int(input().strip())

for q_itr in range(q):
    _ = input().rstrip()
    a = tuple([int(x) for x in input().rstrip().split()])
    result = _triangle(a)
    print(result)