#https://codeforces.com/gym/521377/problem/H?locale=ru
from functools import lru_cache


def _check_bit(i, n):
    return i & (1<<n)
   
def _check_square(i,j,k, jj):
    if _check_bit(i, i+jj+1) or _check_bit(j, i+jj+1) or _check_bit(k, i+jj+1):
       return True
    if _check_bit(j, 0) or _check_bit(j, 1) or _check_bit(j, 2):
       return True
    return False

@lru_cache
def _is_possible(i, j, k, n):
    return all([_check_square(i,j,k,jj) for jj in range(n-3)])

@lru_cache
def _count_nulls ( i, n ) :
    return sum([1 for x in range(n) if not _check_bit(i, x)])

def _spiders(n, m):
    _dp=[[0 for _ in range(n)] for _ in range(n)]
    _profiles=[[0 for _ in range(n)]]
    for ii in range(m):
        for i in range(2**n):
            for j in range(2**n):
                _max=0
                for k in range(2**n):
                    if _is_possible(i<<1, j<<1, k<<1, n+2):
                        if _max<_dp[k][i]:
                            _max=_dp[k][i]
                        _dp[i][j]=_dp[i][j]+_max+_count_nulls(i, n)
    
    _dp=[[ 0 for _ in range(2**n)] for _ in range(m)]
    _dp[0] = [1 for _ in range(2**n)]
    _sum=0
    for ii in range(1, m):
        for i in _dp:
            for j in _dp:
                if _dp[i][j]>0:
                
        return _sum+_dp[i][x]
    return _sum+_dp[i][x]

n,m=tuple([int(x) for x in input().split()])
if n<m:
   n,m=m,n
print()
