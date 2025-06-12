import collections

from sortedcontainers import SortedDict

M = 10 ** 9
_visited=set()
_dp=[]
_closables=[]
def _build_mins(a: list, k: int):
    global _dp
    _dp=[[ -1 for _ in range(k+1) ] for _ in range(len(a))]
    imin = len(a) - 1
    _dp[-1][0] = imin
    for i in range(len(a)-1, k-1, -1):
        imin=i
        for j in range(k, -1, -1):
            if a[imin]>=a[i-j]:
               imin=j
            _dp[i-j][j]=imin


def _build_cache(a: list, k: int):
    global _closables
    _cache=collections.defaultdict(set)
    for i, x in enumerate(a):
        _cache[x].add(i)
    _cache=SortedDict(_cache)

def _visit(a, i):
    _visited.add(i)
    _closables[a[i]].remove(i)

def _pop_min(i, j):
    global _visited
    for x in _closables:
        for ii in _closables[x]:
            if i<=ii<=j:
                _visit(a, ii)
                return ii
    return None

def _count_string_permutation(a: list, k: int)->list:
    i=0
    res=[-1]*len(a)
    _build_cache(a, 2*k)
    while i<len(a):
        if i>=k and (i-k) not in _visited:
            res[i]=a[i-k]
            _visit(a, i-k)
            i+=1
            continue
        imin=_pop_min(max(0, i-k), min(i+k, len(a)-1))
        res[i]=a[imin]
        i+=1
    return res



if __name__ == '__main__':
    k = int(input().rstrip())
    a = list([ord(x) for x in input().rstrip()])
    result = _count_string_permutation(a, k)
    print("".join([chr(i) for i in result]))



