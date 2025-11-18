# https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=32&id_topic=57&id_problem=1049

def try_kun(a: list, t:int, mt:list, i:int=0, visited=None, p=None):
    if visited is None:
        visited = []
    if visited[i]:
        return False


    visited[i] = True

    for to in a[i]:
        if mt[to] == -1 or try_kun(a=a, t=t, i=mt[to], mt=mt, visited=visited):
           mt[to]=i
           return True

    return False

def solve(a:list, _t):
    res=[-1]*_t
    visited = [False] *len(a)

    for i in range(len(a)):
        try_kun(a=a, t=_t, i=i, mt=res, visited=visited)

    words=[-1]*len(a)

    for i,x in enumerate(res):
        if x !=-1:
            words[x]=i+1

    return all(x>0 for x in words), words




_t=int(input().rstrip())
name=input().rstrip()

a=[set() for _ in range(len(name))]

for i in range(_t):
    s=input().rstrip()
    for j, x in enumerate(name):
        if x in s:
            a[j].add(i)

ans=solve(a, _t)
if ans[0]:
    print("YES")
    print(*ans[1])
else:
    print("NO")
