#https://codeforces.com/gym/521377/problem/B
def _is_upper(ch):
    return 'A'<=ch<='Z'


def _letter (s: str):
    _suffix=[0] * len(s)
    _prefix=[0] * len(s)
    for i in range(len(s)-2, -1, -1):
           _suffix[i]=_suffix[i+1]+_is_upper(s[i+1])
    for i in range(1, len(s)):
            _prefix[i]=_prefix[i-1]+(not _is_upper(s[i-1]))
    return min([_prefix[i]+_suffix[i] for i in range(len(s))])
        
    
s=input()
print(_letter(s))