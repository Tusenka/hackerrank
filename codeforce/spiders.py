#https://codeforces.com/gym/521377/problem/H?locale=ru
from copy import deepcopy
from functools import lru_cache , reduce


def _check_bit(i, n):
    return i & (1<<n)
   
def _check_square(i, j, k, jj):
    if _check_bit(i, jj+1) or _check_bit(j, jj+1) or _check_bit(k, jj+1):
       return True
    if _check_bit(j, 0) or _check_bit(j, 1) or _check_bit(j, 2):
       return True
    return False

@lru_cache
def _is_possible(i, j, k, n):
    return all([_check_square(i,j,k,jj) for jj in range(n-2)])

@lru_cache
def _count_nulls ( i, n ) :
    return sum([1 for x in range(n) if not _check_bit(i, x)])

def _spiders(n, m):
    _dp=[[-1 for _ in range(2**n)] for _ in range(2**n)]
    _dp2=[[-1 for _ in range(2**n)] for _ in range(2**n)]
    if n>1:
        for i in range(2**n):
            _dp[i][0]=_count_nulls(i, n)
            _dp2[i][0]=_count_nulls(i, n)
    for ii in range(m):
        for i in range(2**n):
            for j in range(2**n):
                _max=-1
                for k in range(2**n):
                    if _is_possible(i<<1, j<<1, k<<1, n+2):
                        print(i<<1, j<<1, k<<1, n+2)
                        if _max<_dp2[j][k]:
                            _max=_dp2[j][k]
                if ii==m-1 and _max>=0:
                    _dp[i][j]=_max
                elif _max>=0:
                    _dp[i][j]=_max+_count_nulls(i, n)
            if ii==m-1:
                break
        _dp2=deepcopy(_dp)
    return max([x for x in _dp[0] if x>0] or [0])
    
n,m=tuple([int(x) for x in input().split()])
if n<m:
   n,m=m,n
print(_spiders(n, m))
