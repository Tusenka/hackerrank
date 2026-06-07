def solve(a: list):
    s=[0]*len(a)
    s[-1]=a[-1]

    for i in range(len(a)-2, -1,-1):
        s[i]=min(s[i+1], a[i])


    h=[0]*(max(s)+1)
    for x in s:
        h[x]+=1

    return sum(a)-sum(s)+max(h)-1




t=int(input())

for _ in range(t):
    input()
    a=list(map(int, input().split()))

    print(solve(a=a))