# https://codeforces.com/group/sNzo7JKQN1/contest/527247/problem/B
from __future__ import annotations
import dataclasses

M=10**9

@dataclasses.dataclass
class Edge:
    source: int
    destination: int
    weight: int


@dataclasses.dataclass
class Stat:
    weight: int =0
    rank: int =0
    node_id: int =0

@dataclasses.dataclass
class TreeNode:
    val: int = 0
    rank: int = 0
    child: list[Edge]= dataclasses.field(default_factory=list)
    parents: list[Stat]=dataclasses.field(default_factory=list)

    __q:list[TreeNode]=dataclasses.field(default_factory=list)

def _solve_for_node(node: TreeNode)->Stat | None:
    r=0
    last=0

    while r<len(node.parents):
        if node.parents[r].weight<=node.val:
           if r>=len(node.parents)-1 or node.parents[r+1].weight>node.val:
               return node.parents[r]
           last=r
           r=r<<1 if r else 1
        elif last<r:
           r=last+1
           last=r
        else:
            return None

    return None

def solve(a: list, edges: list[Edge]) -> list[Stat]:
   n=len(a)
   tree=_prepare(edges=edges, a=a)
   res=[Stat(0,0, 0)]*n

   for i, node in enumerate(tree):
       res[i]=_solve_for_node(node=node)

   return res

def _prepare(edges: list[Edge], a: list[int]) -> list[TreeNode]:
    res=[TreeNode(val=val) for val in a]

    for edge in edges:
        res[edge.source].child.append(edge)

    queue=[(0,0)]

    # prepare hashes
    while queue:
        node=queue.pop(0)
        res[node[0]].rank=node[1]
        for child in res[node[0]].child:
            queue.append((child.destination, node[1]+1))
            res[child.destination].parents=[Stat(rank=node[1], weight=child.weight, node_id=node[0])]+[Stat(rank=stat.rank, weight=stat.weight+child.weight, node_id=stat.node_id) for stat in res[node[1]].parents]

    return res



n=int(input())

a=list(map(int, input().split()))
edges=[]

for d in range(1, n):
    s, v =tuple(map(int, input().split()))
    edges.append(Edge(source=s-1, destination=d, weight=v))

print(solve(a, edges))