# Driver Code
adj = [ [ 0, 1, 1, 1, 0 ] ,
        [ 1, 0, 1, 0, 1 ],
        [ 1, 1, 0, 1, 1 ],
        [ 1, 0, 1, 0, 0 ] ]

N = len(adj)
M = 1000000007


def _check_bit(i, j):
    return i&(1 << j)


def _hamilton(adj):
    n=len(adj)
    _dp=[[M for _ in range(n)] for _ in range(1<<n)]
    for i in range(n):
        _dp[1<<i][i]=0

    for j in range(n):
        for i in range(1<<n):
            if _check_bit(i, j) or True:
                _min=M
                for k in range(n):
                    if adj[j][k] and j!=k and _check_bit(i, k) and _dp[i^(1<<j)][k]<M:
                        if _min>adj[j][k]:
                            _min=adj[j][k]+_dp[i^(1<<j)][k]
                _dp[i][j]=_min
    return min(_dp[-1])



def hamiltonian_path(adj):
    return _hamilton(adj)



n=int(input())
adj=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    adj[i]=list(map(int, input().split()))
print(hamiltonian_path(adj))
