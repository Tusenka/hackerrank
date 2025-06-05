#https://codeforces.com/contest/2116/problem/B
from functools import lru_cache

M=998244353
@lru_cache
def _eval_sum(p, q):
    return ((1<<p)+(1<<q)) % M

@lru_cache
def _eval_r(p: tuple, q: tuple):
      r=[1]*len(p)
      r[0]=_eval_sum(p[0], q[0])
      for i in range(1, len(p)):
          r[i]=max([_eval_sum(p[j], q[i-j]) for j in range(i+1)])
      return r
t=int(input())
for _ in range(t):
    _=input()
    p=tuple(int(x) for x in input().split())
    q=tuple(int(x) for x in input().split())
    print(*_eval_r(p, q ))

          
    
    

