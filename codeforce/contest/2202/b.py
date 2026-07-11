def solve(s:str):
    if len(s)%2==1:
        if s[0]=='b':
            return False

        s=s[1:]
    if s[0]==s[1]:
        return False
    for i in range(1, len(s)//2):
        if s[2*i]==s[i*2-1] and s[2*i]!='?':
            return False
    return True


t = int(input())

for _ in range(t):
    input()
    s=input()

    print("YES" if solve(s) else "NO")
