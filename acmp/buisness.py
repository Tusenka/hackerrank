_dp=[]

def count_profit(a: list):
    global _dp
    _dp = [-1] * len(a)
    imax=len(a)-1
    _dp[-1]=imax
    for i in range(len(a)-2, -1, -1):
        if a[i]>a[imax]:
            imax=i
        _dp[i]=imax
    _sum = 0
    n=1
    for j in range(len(a)):
        if _dp[j]==j:
            _sum+=a[j] * n
            n=1
        else:
            n+=1
    return _sum


if __name__ == '__main__':
    (n) = tuple([int(x) for x in input().rstrip().split()])
    a = list([int(x) for x in input().rstrip().split()])
    result = count_profit(a)
    print(result)



