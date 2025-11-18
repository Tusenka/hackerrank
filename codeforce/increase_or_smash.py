#https://codeforces.com/contest/2152/problem/A
def solve(a: list):
    a=sorted(set(a), reverse=True)
    if a[0]==0:
        return 0
    if len(a)==1:
        return 1
    count=0
    while True:
        if len(a)==0:
            break
        x=a[-1]
        del a[-1]
        a=[v-1 for v in a]
        count+=2
    return count-1


t = int(input().rstrip())

for _ in range(t):
    n=int(input().rstrip())
    a= list(map(int, input().rstrip().split()))
    print(solve(a))