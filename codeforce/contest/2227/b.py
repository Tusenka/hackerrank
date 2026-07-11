def solve(s: str):
    c=0

    for x in s:
        if x=='(':
           c+=1
        else:
           c-=1

    return c==0

t=int(input())

for _ in range(t):
    input()
    s=input()
    print("YES" if solve(s) else "NO")