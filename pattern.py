from functools import cache, lru_cache

_profiles11={}
_profiles00={}

def _build_profiles(N):
    global _profiles11
    _profiles={ x: set() for x in [_bin_to_str(i, N) for i in range(2**N)] if '11' in x }
    _profiles11={ x: set() for x in [_bin_to_str(i, N) for i in range(2**N)] if '11' in x }
    _profiles00={ x: set() for x in [_bin_to_str(i, N) for i in range(2**N)] if '00' in x }
    for s in _profiles11:
            j=-1
            while True:
                j=s.find(s ,j+1)
                if j<0:
                    break
                else:
                    _profiles11[s].add(j)

    for s in _profiles00:
            j=-1
            while True:
                j=s.find(s ,j+1)
                if j<0:
                    break
                else:
                    _profiles00[s].add(j)

def _bin_to_str(n, len):
    return str(bin(n))[2:].zfill(len)


@lru_cache
def _next_profiles11(p: str):
    global _profiles11
    if p not in _profiles11:
        return []
    return [s for s in _profiles11 if _profiles11[s].intersection(_profiles11[p])]

@lru_cache
def _next_profiles00(p: str):
    global _profiles00
    if p not in _profiles00:
        return []
    return [s for s in _profiles00 if _profiles00[s].intersection(_profiles00[p])]

_dp=[]
def _pattern(n, m):
    _build_profiles(n)
    global _profiles
    _count=0
    _dp=[dict() for _ in range(m) ]
    _dp[0]={ x: 1 for x in _profiles}
    for i in range(1,m):
        for s in _profiles:
            _profile=list(_next_profiles11(s))
            _dp[i][s]=sum([_dp[i-1][p] for p in _profiles])
    return sum(_dp[m-1].values())


n, m = tuple([int(x) for x in input().rstrip().split()])
print((2**n)**m-_pattern(n,m))
