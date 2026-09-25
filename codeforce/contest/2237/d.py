def build_ps(s):
    ps=[0]*(len(s)+1)
    if len(s)==1:
        return ps

    ps[1]=1 if s[0]=='1' else -1

    for i in range(1, len(s)):
        ps[i+1]=((ps[i]+1) if s[i]=='1' else (ps[i]-1)) %3

    return ps


def solve(s: str):
    ps=build_ps(s=s)
    if len(s)==1:
        return 1

    c=0
    i=1
    l=1
    h=[-1]*4
    h[0]=1
    while i<len(s)+1:
        if s[i]==s[i-1]:
           l+=1


    return c



t=int(input())

for _ in range(t):
    input()
    s=input()
    print(solve(s))