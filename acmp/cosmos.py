import itertools
_dp=[]
def _recovery_indexes(_dp:list, *, a, t, f, i:int=-1, ans=None):
    if ans is None:
        ans = set()
    if i==-1:
       i=len(_dp)-1
    if _dp[i][t][f]==0:
        return
    if _dp[i-1][t][f]<_dp[i][t][f]:
        ans.add(i)
        _recovery_indexes(_dp, a=a, f=f - a[i - 1]['f'], t=t - a[i - 1]['t'], i=i - 1, ans=ans)
    else:
        _recovery_indexes(_dp, a=a, f=f, t=t, i=i - 1, ans=ans)
    return ans


def cosmos(a:list, F:int, T:int):
    global _dp
    for i, x in enumerate(a):
        for t, f in itertools.product(range(T, x['t'] - 1, -1), range(F, x['f']-1, -1)):
            _dp[i+1][t][f] = max(_dp[i][t][f], _dp[i][t-x['t']][f-x['f']]+x['v'])
    _cache=_recovery_indexes(_dp, a=a, f=F, t=T)
    return _dp[-1][-1][-1], _cache #max


if __name__ == '__main__':
    (n, F, T) = tuple(int(x) for x in input().rstrip().split())
    a=[]
    for _ in range(n):
        (vi, fi, ti ) = tuple(int(x) for x in input().rstrip().split())
        a.append({'f': fi, 't': ti,'v': vi})
    _dp = [[[ 0 for _ in range(F+1)] for _ in range(T+1)] for _ in range(n+1)]
    result = cosmos(a, F, T)
    print(result[0])
    if result[0]>0:
       print(sorted(result[1]))



