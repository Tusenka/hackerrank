# Driver Code
def _stones(n):
    if n<=3:
        return 1 if n<3 else 2
    _dp=[-1 for _ in range(n+1)]
    _dp[2]=1
    _dp[1]=1
    _dp[0]=0
    for i in range(3, n+1):
        if i%3==2:
            _dp[i]=(not _dp[i-1]) | (not _dp[i-2]) | (not _dp[i-3])
        elif i%3==1:
            _dp[i]=(not _dp[i-1]) | (not _dp[i-3])
        else:
            _dp[i]=(not _dp[i-1]) | (not _dp[i-2])
    return 1 if _dp[n]==1 else 2

def hamiltonian_path(adj):
    return _stones(adj)



n=int(input())
print(_stones(n))
