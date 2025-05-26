#https://codeforces.com/gym/521377/problem/B
def _is_upper(ch):
    return 'Z'<=ch < 'A'
    

def _letter (s: str) :
    _suffix=[0] * len(s)
    _prefix=[0] * len(s)
    for i in range(len(s)-2, -1):
        if _is_upper(s[i]):
           _suffix[i]=_suffix[i+1]+1
        else:
            _suffix[i]=_suffix[i+1]
    for j in range(1, len(s)):
    
        if not _is_upper(s[j+1]):

        
    
s=input()
print(_letter(s))