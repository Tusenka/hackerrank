M = 300 * '.'

def _build_seq(r, v):
    global _dp
    if len(r)==len(v)==0:
        return 0
    if r[-1]==v[-1] or v[-1]=="*" or v[-1]=="?":
        _dp[-1][-1]=r[-1]
    if r[-1]=="*" or r[-1]=="?":
        _dp[-1][-1]=v[-1] if v[-1]!='?'and v[-1]!='*' else 'A'
    if _dp[-1][-1]==M:
        return _dp
    for i in range(len(r)-2, -1, -1):
        if r[i]=='*':
            _dp[i][-1]=v[i]+_dp[i+1][-1]
        elif v[i]=='*':
            _dp[i][-1]=r[i]+_dp[i+1][-1]
        else:
            break
    for i in range(len(r) - 2, -1, -1):
        for j in range(len(v) - 2, -1, -1):
            if r[i]=='*':
                _dp[i][j]=min(v[j]+_dp[i][j+1], v[j]+_dp[i+1][j+1], _dp[i+1][j], key=lambda x: len(x))
            elif v[i]=='*':
                _dp[i][j]=min(r[i]+_dp[i+1][j],r[i]+_dp[i+1][j+1], _dp[i][j+1], key=lambda x: len(x))
            elif (r[i]=='?' or r[i]==v[j] or v[j]=='?') and len(_dp[i+1][j+1])<300:
                _dp[i][j]=(r[i] if r[i]!='?' else v[j]) +_dp[i+1][j+1]
            else:
                break
    return _dp[0][0] if len(_dp[0][0])<300 else ''


if __name__ == '__main__':
    a = input().rstrip()
    b = input().rstrip()
    _dp=[[ M for _ in range(len(b))] for _ in range(len(a))]
    res=_build_seq(a, b)
    print(res)