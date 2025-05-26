# https://informatics.msk.ru/mod/statements/view.php?id=655&chapterid=113079#1

def _phers(n, m):
    _dp=[[-1 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        _dp[0][i]=1
    for j in range(n):
        _dp[j][0]=1
    for i in range(min(n,m)):
        _dp[i][i]=1
    for i in range(1, n):
        for j in range(1, m):
                if i==j:
                    _dp[i][j]=1
                else:
                    _dp[i][j]=any(not _dp[i][x] for x in range(j)) or any (not _dp[x][j] for x in range(i))
    return 1 if _dp[n-1][m-1]==1 else 2

n, m=tuple(map(int, input().split()))
print(_phers(n,m))
