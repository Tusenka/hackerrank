def recover_indexes(a: list, _dp: list):
    indexes=set()
    w=len(_dp[0])-1
    for i in range(len(_dp)-1, 0 , -1):
        if _dp[i][w]>_dp[i-1][w]:
            indexes.add(i)
            w-=a[i][0]
    if _dp[0][w]>0:
        indexes.add(0)
    return indexes


def backpack(a:list, w:int):
    _dp=[[0 for _ in range(w+1)] for _ in range(len(a))]
    _dp[0]=[ a[0][1] if a[0][0]<=wi else 0 for wi in range(w+1)]
    for i in range(1, len(a)):
        for wi in range(w, 0, -1):
            if wi-a[i][0]>=0:
               _dp[i][wi]=max(_dp[i-1][wi-a[i][0]]+a[i][1], _dp[i-1][wi])
            else:
               _dp[i][wi]=_dp[i-1][wi]
    return _dp

if __name__ == '__main__':
    (n, W) = tuple([int(x) for x in input().rstrip().split()])
    a = []
    wi = tuple([int(x) for x in input().rstrip().split()])
    pi = tuple([int(x) for x in input().rstrip().split()])
    for i in range(n):
        a.append((wi[i], pi[i]))
    result=backpack(a,  W)
    indexes=recover_indexes(a, result)
    for x in indexes:
        print(x+1)
