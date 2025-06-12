M = -10 ** 9 + 7
def _build_seq(n, a1, k, b, m):
    a=[a1]
    for i in range(1, n):
        a.append((k*a[i-1]+b) % m)
    return a

def _eval_seq(a: tuple):
    a=tuple([M]+list(a))
    _dp=[ -1 for _ in range(len(a)+1)]
    _dp[0]=0
    _dp[1]=1
    for i in range(len(a)):
        for j in range(len(a)-2, -1, -1):
            if _dp[j]>-1 and a[i]>a[_dp[j]]:
               if _dp[j+1]<0:
                  _dp[j+1]=i
                  break
               else:
                  if a[_dp[j+1]]>a[i]:
                     _dp[j+1]=i
               break
    for i in range(len(a), -1, -1):
        if _dp[i]>0:
            return i



if __name__ == '__main__':
    n, a1, k, b, m = tuple([int(x) for x in input().rstrip().split()])
    a=tuple(_build_seq(n, a1, k, b, m))
    print(_eval_seq(a))