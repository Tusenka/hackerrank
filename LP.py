M = -10 ** 9 + 7
def _match(s, i, j):
    if s[i]=='{' and s[j]=='}':
        return 2
    if s[i]=='(' and s[j]==')':
        return 2
    if s[i]=='[' and s[j]==']':
        return 2
    return 0

def _out(s, _dp, i, j):
    if _dp[i][j]==0:
        return ''
    if i>=j:
       return ''
    for k in range(i,j):
        if _dp[i][j]==_dp[i][k]+_dp[k][j] and (_dp[i][k]>0 or _dp[j][k]>0):
            return _out(s, _dp, i, k)+_out(s, _dp, k, j)
    if _dp[i][j]==_dp[i+1][j-1]+2:
       return s[i]+_out(s,_dp, i+1, j-1)+s[j]
    return ''

def _lp(s):
    if s=="":
        return 0
    _dp=[[0 for _ in range(len(s))] for _ in range(len(s))]
    for l in range(len(s)-1, -1, -1):
        _dp[l][l]=0
        for r in range(l+1, len(s)):
            _dp[l][r]=max(_dp[l+1][r-1]+_match(s, l, r), max([_dp[l][k]+_dp[k][r] for k in range(l,r)]))
    return _dp[0][-1]>0, _dp

def lp(s):
    result, _dp = _lp(s)
    if result:
        return _out(s, _dp, 0, len(s)-1)
    else:
        return

s=input().rstrip()
print(lp(s))