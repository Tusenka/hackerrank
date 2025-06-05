from functools import lru_cache


@lru_cache
def _fact(n):
    return 1 if n<=1 else n*_fact(n-1)

@lru_cache
def _binomial(n, k):
    return _fact(n)/(_fact(k)*_fact(n-k))

def _solve(n, k):
    return int(_binomial(n, k)*_binomial(n,k)*_fact(k))

n,k=map(int, input().split())
print(_solve(n,k))
    
    
