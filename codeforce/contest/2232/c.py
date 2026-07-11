def solve(n:int, v:int, s:str):
    h=['A']*len(s)
    i=len(s)-1
    while i>=0 and s[i]=='A':
        i-=1

    if i==-1 and s[0]=='A':
        return n

    h[i]=s[i]

    for j in range(i-1, -1, -1):
        if s[j]!=h[j+1] and s[j]!='A':
           h[j]=s[j]
        else:
           h[j]=h[j+1]

    _count=0
    et=n
    net=[0]*n
    i=n-1
    for j in range(len(s)):
        if s[j]=='I':
           if et:
              et-=1
              net[et]=v-1
              continue
        if s[j]=='E':
            if net[i]:
               net[i]-=1
               continue
            elif i>0 and et<i:
               net[i-1]-=1
               i-=1
               continue

        if s[j]=='A':
           if h[j]=='E' and (not net[i] or not(i>0 and net[i-1])) and et:
                   et-=1
                   net[et]=v-1
                   continue
           if net[i]:
                   net[i]-=1
                   continue
           elif i>0 and net[i-1]:
               i-=1
               net[i]-=1
               continue
           if et:
               et-=1
               net[et]=v-1
               continue
        _count+=1

    return len(s)-_count


t=int(input())

for _ in range(t):
    _, n,v=tuple(map(int, input().split()))
    s=input()
    print(solve(n=n,v=v, s=s))