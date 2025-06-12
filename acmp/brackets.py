from functools import cache

_closables=[]
_dp={}
def build_closed(s: str):
    global _closables
    _closables= [0] * len(s)
    _closables[-1]=int(s[-1] != '(')
    for i in range(len(s)-2, -1, -1):
        if s[i]!='(':
            _closables[i]= _closables[i + 1] + 1
        else:
            _closables[i]=_closables[i + 1]

@cache
def _find_count(s, i, state):
    global _closables
    if state>_closables[i]:
        return 0
    if state<0:
        return 0
    if i==len(s)-1:
       if state>1 or state==0 or s[i]=='(':
            return 0
       else:
           return 1
    if s[i]=='(' or state==0:
        return _find_count(s, i+1, state+1)
    if s[i]==')':
        return _find_count(s, i+1, state-1)
    else:
        return _find_count(s, i+1, state+1)+ _find_count(s, i+1, state-1)


def seq(s):
   build_closed(s)
   if s[-1]=='(':
        return 0
   return _find_count(s, 0, 0)

if __name__ == '__main__':
    s = input().rstrip()
    print(seq(s))
