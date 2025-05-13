M = 10**9 + 7

def _recovery_indexes(a:list, _dp: list):
    a0=[]
    a1=[]
    a2=[]
    i=j=sum(a)//3
    while (i>0 or j>0) and (i>=0 and j>=0):
            assert _dp[i][j]!=0
            if _dp[i][j]==-M:
                break
            if _dp[i][j]>0:
                a1.append(_dp[i][j])
                i-=_dp[i][j]
            else:
                a2.append(-_dp[i][j])
                j+=_dp[i][j]
    a0=filter(lambda x: x not in a1 and x not in a2, a)
    return a0, a1, a2


def three_knapsack(a:list):
    a.sort(reverse=True)
    w=sum(a)
    if w%3!=0:
        return 1
    else:
        w=w//3
    _dp=[[ 0 for _ in range(w+1)] for _ in range(w+1)]
    _dp[0][0]=-M
    for x in a:
        for i in range(w, -1, -1 ):
            for j in range(w, -1, -1):
                if _dp[i][j]!=0:
                    continue
                if i>=x and  _dp[i-x][j]!=0:
                    _dp[i][j]=x
                elif j>=x and _dp[i][j-x]!=0:
                    _dp[i][j]=-x
    return _dp[w][w]!=0, _dp


if __name__ == '__main__':
    _ = input()
    a = list([int(x) for x in input().rstrip().split()])
    result, _dp=three_knapsack(a)
    if result:
        a0, a1, a2 = _recovery_indexes(a, _dp)
        print(*a0)
        print(*a1)
        print(*a2)
    else:
        print("No solution")