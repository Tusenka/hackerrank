_dp={}
def _find_numbers(x:int, m:int):
    global _dp
    if x in _dp:
       return _dp[x]
    if x==1:
        return 1
    ans=0
    for y in range(1, x):
        ans+=_find_numbers(y,m)
    for z in range(2, x+1):
        ans+=_find_numbers(x//z, m)
    _dp[x]=ans
    return ans % m

if __name__ == '__main__':
    (x, n) = tuple([int(x) for x in input().rstrip().split()])
    print(_find_numbers(x, n))




