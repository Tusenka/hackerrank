from collections import defaultdict
from functools import cache
from typing import DefaultDict

M = 10 ** 9 + 7
_steps={0: (6, 4), 1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (3, 9, 0), 5:(), 6: (1, 7, 0), 7: (2, 6), 8: (1, 3), 9: (2, 4)}
_dp=defaultdict(lambda: defaultdict(int))

def _build_dp(l: int):
    global _dp
    for i in _steps.keys():
        _dp[1][i]=1
    for n in range(2, l+1):
        for i in _steps.keys():
            _dp[n][i]=sum(_dp[n-1][x] for x in _steps[n])
    return sum(_dp[l][x] for x in _steps.keys() if (x!=8 and x!=0))

if __name__ == '__main__':
    n = int(input().rstrip())
    print(_build_dp(n))
