def solve(s: str):
    _max=0
    l=0
    r=0
    if '#' not in s:
        return 0

    while l<len(s) and r<len(s):
        c=0
        r=l
        while r<len(s) and s[r]=='#':
            c+=1
            r+=1
        l=r if r>l else l+1
        _max=max(c, _max)

    if  _max%2:
        return max(1, _max//2+1)
    else:
        return max(1, _max//2)



t=int(input())

for _ in range(t):
    input()
    s=input()

    print(solve(s=s))