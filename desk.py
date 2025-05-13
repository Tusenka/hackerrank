from collections import defaultdict

M = 10 ** 9 + 7

def _desk(c):
    c.sort()
    if len(c)==0:
        return 0
    _dp=defaultdict(lambda:defaultdict(lambda:M))
    for i in range(len(c)-1):
        _dp[c[i]][c[i+1]]=0
        _dp[c[i]][c[i]]=0
    for i in range(len(c)-1, -1, -1):
        for j in range(i+2, len(c)):
            l=c[i]
            r=c[j]
            _dp[l][r]=min([_dp[l][c[k]]+_dp[c[k]][r] for k in range(i,j)])+r-l
    return _dp[c[0]][c[-1]]

def desk(c, l):
    c0=[0]+c+[l]
    return _desk(c0)

l, n=tuple([int(x) for x in input().rstrip().split()])
c=[int(x) for x in input().rstrip().split()]
print(desk(c, l))