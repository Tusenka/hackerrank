from collections import defaultdict

M = 10 ** 9 + 7

def _desk(c):
    c.sort()
    if len(c)==0:
        return 0
    _dp=[[(M, -1) for _ in range (len(c))] for _ in range(len(c)) ]
    for i in range(len(c)-1):
        _dp[i][i+1] = (0, i+1)
        _dp[i][i] = (0, i)
    for i in range(len(c)-1, -1, -1):
        for j in range(i+2, len(c)):
            l=c[i]
            r=c[j]
            t1=_dp[i][j-1]
            t2=_dp[i+1][j]
            _min=M
            _imin=i
            for k in range(t1[1], t2[1]+1):
                if _dp[i][k][0]+_dp[k][j][0]<_min:
                    _imin=k
                    _min=_dp[i][k][0]+_dp[k][j][0]
            _dp[i][j]=(r-l+_min, _imin)
    return _dp[0][-1][0]

def desk(c, l):
    c0=[0]+c+[l]
    return _desk(c0)

l, n=tuple([int(x) for x in input().rstrip().split()])
c=[int(x) for x in input().rstrip().split()]
print(desk(c, l))