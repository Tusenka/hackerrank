M = 10 ** 9 + 7

def _build_seq(r, v):
    global _dp
    if len(r)==len(v)==0:
        return 0
    #if len(r)==len(v):
    #   return len(r) if all([r[i]=='?' or r[i]=='*' or r[i]==v[i] for i in range(len(r))]) else 0
    _dp[0][0]=M
    _dp[-1][-1]=r[-1] if r[-1]==v[-1] or r[-1]=="*" or r[-1]=='?' or v[-1]=="*" or v[-1]=="?" else M
    if _dp[-1][-1]=='':
        return M
    for i in range(len(r)-2, -1, -1):
        if r[i]=='*' or v[-1]=='*':
            _dp[i][-1]=_dp[i+1][-1]+1
        else:
            _dp[i][-1]=M

    for i in range(len(r) - 2, -1, -1):
        for j in range(len(v) - 2, -1, -1):
            if r[i]=='*':
                _dp[i][j]=min(_dp[i][j+1]+1, _dp[i+1][j+1]+1, _dp[i+1][j])
            elif v[i]=='*':
                _dp[i][j]=min(_dp[i+1][j]+1, _dp[i+1][j+1]+1 or _dp[i][j+1])
            elif r[i]=='?' or r[i]==v[j] or v[j]=='?':
                _dp[i][j]=_dp[i+1][j+1]+1
            else:
                _dp[i][j]=M
    return _dp[0][0]



if __name__ == '__main__':
    a = input().rstrip()
    b = input().rstrip()
    if '*' in b or '?' in b:
        a, b= b, a
    _dp=[[ '' for _ in range(len(b))] for _ in range(len(a))]
    res=_build_seq(a, b)
    print(res if res<M else 0)