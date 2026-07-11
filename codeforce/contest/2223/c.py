def solve(a1, a2):
    n=len(a1)

    p=0
    diff=0
    for i in range( n):
        if a1[i]=='(' and a2[i]=='(':
           p+=2
        elif a1[i]==')' and a2[i]==')':
           p-=2
        else:
           diff+=1

        if diff%2 and p<2:
           return False

        if p<0:
            return False
    if p:
        return False

    return True


t=int(input())

for _ in range(t):
    input()
    a1=list(input().strip())
    a2=list(input().strip())

    print("YES" if solve(a1=a1,a2=a2) else "NO")

