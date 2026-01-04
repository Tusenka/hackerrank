from __future__ import annotations

import dataclasses
from collections import deque


#https://codeforces.com/problemset/problem/2182/G
@dataclasses.dataclass
class Tree:
    p: Tree | None= None
    children: list[Tree]= dataclasses.field(default_factory=list)
    i: int = 0
    d: int = 0

def solve(p: list[int], k: int):
    nodes= [Tree(i=i) for i in range(len(p)+1)]
    for i in range(1, len(p)+1):
        nodes[p[i]-1].children.append(nodes[i])
        nodes[i].p=nodes[p[i]-1]

    dp=[[-1 for _ in range(2)] for _ in range(len(p)+1)]
    dfs(root=nodes[0], dp=dp)

    #dp[i+1]=dp[i+1]+



def dfs(root: Tree, dp:list[list[int]]):
    q=deque()
    q.append((root,0))
    dp[0]=[-1,-1]

    while q:
        el=q.popleft()
        node, d=el

        for child in node.children:
            q.append((child, d+1))
            q.d=d+1
            if len(node.children)>1:
                dp[child.i][0]=node.i
            else:
                dp[child.i][0]=dp[node.i][0]


t = int(input())
for _ in range(t):
    _,k=tuple(map(int, input().split()))
    p=list(map(int, input().split()))
    print(solve(p=p, k=k))