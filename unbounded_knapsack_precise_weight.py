def backpack(a:list, w:int, k: int):
    _dp=[[0 for _ in range(w+1)] for _ in range(len(a))]
    _dp[0]=[ a[0][1] if a[0][0]<=wi else 0 for wi in range(w+1)]
    for i in range(1, len(a)):
        for wi in range(w, 0, -1):
            if wi-a[i][0]>=0:
                _dp[i][wi]=max(_dp[i-1][wi-a[i][0]]+a[i][1], _dp[i-1][wi])
            else:
               _dp[i][wi]=_dp[i-1][wi]
    return _dp
