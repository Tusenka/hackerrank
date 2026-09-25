def solve(s,c):
    i=0
    j=len(s)-1
    ans=0
    while i<j:
        if s[i]==s[j]:
           i+=1
           j-=1
           continue

        if s[i]==c or s[j]==c:
            ans+=1
        else:
            ans+=2
        i+=1
        j-=1

    return ans

t=int(input())

for _ in range(t):
    _,c=tuple(input().split())
    s=input()
    print(solve(s=s, c=c))
