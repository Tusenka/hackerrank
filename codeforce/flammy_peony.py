#https://codeforces.com/contest/2116/problem/B
from functools import lru_cache
import math

@lru_cache
def _gcd(p, q):
    return math.gcd(p, q)

@lru_cache
def _agcd(*args):
    return math.gcd(*args)

def _equal(q:list):
    return (q[0]==q[-1])
    #return len(set(q))==len(q)

def _equality(q: list):
    return len(q)-len(set(q))

def _eval_r(q: list):
      q.sort()
      _count=0
      _eq=_equality(q)
      changed=False
      _min=_agcd(*q)
      for i in range(len(q)):
      while True:
        for i in range(len(q)):
            for j in range(len(q)-1, i):
                if i==j:
                    continue
                _new=_gcd(q[i], q[j])
                if _new==_min:
                    _count+=1
                    q[i]=_new
                    q[j]=_new
        if _equal(q):
            return _count
        if not changed:
           q[-1]=_gcd(q[-1], q[0])
           q.sort()
           _count+=1
           _eq=_equality(q)

t=int(input())
for _ in range(t):
    _=input()
    q = [int(x) for x in input().split()]
    print(_eval_r(q))

          
    
    

