from collections import deque


def solve(e: list[int], w: list[int]):
    m=[0 for _ in e]
    q=deque()
    for x in w:
        q.append(x)
    while q:
        i=q.popleft()
        m[i]+=1
        if e[i]==0 or i==0:
           continue
        q.append(e[i])

    for x in e:
        q.append(x)

    ans=set()
    while q:
        i=q.popleft()
        if not m[i]:
            continue
        if e[i]==i==0:
            continue
        ans.add((i,e[i]))
        if e[i]:
            q.append(e[i])

    return ans

t=int(input())

for _ in range(t):
    input()
    e=[0]+list(map(lambda x: int(x)-1, input().split()))
    input()
    w=list(map(lambda x: int(x)-1, input().split()))
    ans=solve(e, w)
    print(len(ans))
    for x in ans:
        print(*x)