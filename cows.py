import heapq
import collections



def _get_cube_length(a: list):
    _cache={}
    _max_range=0
    _last=a[0]
    _c=0
    for x in a:
        if _last==x:
            _c+=1
        elif x is None:
            continue
        else:
            _c=0
            _last=x
        if _max_range<_c:
            _max_range=_c
    return _max_range

def _del(a, i):
    return a[0:i]+a[i+1:]


def _check_cache(_cache: list, imax: int, k):
    _sum=0
    for i, v in enumerate(_cache):
        if i==imax:
           continue
        _sum+=v
        if _sum>k:
            return False
    return True


def _build_cube(a: list, k:int, m: int):
    for i in range(len(a)):
        a[i]-=1
    _heap=[collections.defaultdict(int) for _ in range(len(a))]
    for x in a:
        _heap[0][x]+=1
    _cache=[0]*m
    _cache[a[0]]=1
    _heap[1][a[0]]+=1
    _heap[0][a[0]]-=1
    _max_range=1
    ilen=1
    l=0
    for r in range(1, len(a)):
        _cache[a[r]]+=1
        _heap[_cache[a[r]]][a[r]]+=1
        _heap[_cache[a[r]]-1][a[r]]=-1
        if ilen<_cache[a[r]]:
            ilen=_cache[a[r]]
        imax=next(iter(_heap[ilen]))
        while not _check_cache(_cache, imax, k) and l<r:
            l+=1
            _cache[a[l-1]]-=1
            _heap[_cache[a[l-1]]][a[l-1]]=-1
            _heap[_cache[a[l-1]]-1][a[l-1]]=+1
            if _heap[ilen][a[l-1]]==0:
                ilen = _cache[a[l]-1]
                imax=_heap[ilen]
        if r-l+1>_max_range:
            _max_range=r-l+1
    return _max_range


if __name__ == '__main__':
        (n, m, k) = tuple([int(x) for x in input().rstrip().split()])
        a = list([int(x) for x in input().rstrip().split()])

        result = _build_cube(a, k, m)

        print(result)