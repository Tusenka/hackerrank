from functools import lru_cache
profiles=[]
N=0
def build_graph(n):
    global _profiles
    _profiles=[set() for _ in range(2 ** n)]
    for i in range(2**n):
        for j in range(2**n):
            if _check_profiles(i, j, n):
                _profiles[i].add(j)

@lru_cache
def _check_profiles(p1: int, p2: int, n: int):
    for i in range(n-1):
        if check_bit(p1, i) == check_bit(p2, i) == check_bit(p1, i+1) == check_bit(p2,i+1):
            return False
    return True

def check_bit(n, i):
    if (1<<i) & n:
        return 1
    else:
        return 0
    
def eval_profiles(m, n):
    global _profiles
    _dp=[[0 for _ in range(2**n)] for _ in range(m)]
    _dp[0] = [1 for _ in range(2**n)]
    for i in range(1, m):
        for j in range(len(_profiles)):
            _dp[i][j]=sum(_dp[i-1][x] for x in _profiles[j])
    return sum(_dp[-1])


n, m = tuple([int(x) for x in input().rstrip().split()])
if n>m:
    n,m=m,n
print(eval_profiles(m, n))