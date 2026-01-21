def solve(s: str):
    pref=0
    if  len(s)==1:
        return 1
    for i in range(len(s)):
        if s[i]=='1':
            break
        else:
            pref+=1
    else:
        return len(s)//2

    suf=0

    for i in range(len(s)-1, -1, -1):
        if s[i]=='1':
            break
        else:
            suf+=1
    s=s[pref:len(s)-suf]
    if len(s)==1:
        return max(0,suf-1)//2+max(0,pref-1)//2+1

    ps={n:0 for n in range(2,len(s)-1)}

    ans=max(0, suf-1)//2+max(0,pref-1)//2+len([x for x in s if x=='1'])

    for n in reversed(range(2, len(s)-1)):
        if '1'+'0'*n+'1' in s:
            ps[n]+=1

    for n, val in ps.items():
        ans+=(n-2)//2*val

    return ans

t=int(input())

for _ in range(t):
    _=input()
    s=input()

    print(solve(s))
