from collections import defaultdict
from functools import lru_cache , reduce


@lru_cache
def _fact(n):
    return 1 if n<=1 else n*_fact(n-1)

@lru_cache
def _binomial(n, k):
    return _fact(n)/(_fact(k)*_fact(n-k))

def _solve(s):
    _cache=defaultdict(int)
    for i in s:
        _cache[i]+=1
    return int(_fact(len(s))/reduce(lambda x, y: x*y, [_fact(i) for i in _cache.values()]))

s=input()
print(_solve(s))
    
    
