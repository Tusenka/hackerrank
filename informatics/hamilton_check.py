# Driver Code
adj = [ [ 0, 1, 1, 1, 0 ] ,
        [ 1, 0, 1, 0, 1 ],
        [ 1, 1, 0, 1, 1 ],
        [ 1, 0, 1, 0, 0 ] ]

N = len(adj)

def _check_bit(i, j):
    return (i&(1<<j))


def _hamilton(adj):
    n=len(adj)
    _dp=[[False for _ in range(n)] for _ in range(1<<n)]
    for i in range(n):
        _dp[1<<i][i]=True

    for i in range(1<<n):
        for j in range(n):
            if _check_bit(i, j):
                for k in range(n):
                    if adj[j][k] and j!=k and _check_bit(i,k) and _dp[i^(1<<j)][k]:
                        _dp[i][j]=True
                        break
    return any(_dp[1<<n-1])



def hamiltonian_path(adj, N):
    return _hamilton(adj)


if (hamiltonian_path(adj, N)):
    print("YES")
else:
    print("NO")