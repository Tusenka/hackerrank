# https://informatics.msk.ru/mod/statements/view3.php?chapterid=111689#1
import dataclasses
from dataclasses import field

M = 10**9


@dataclasses.dataclass
class Edge:
    end: int
    color: int = 0
    i: int = 0
    skip = False

    def __hash__(self):
        return i

    def __eq__(self, other):
        return self.i == other.i


@dataclasses.dataclass
class Node:
    es: dict[int, Edge] = field(default_factory=dict)
    h: int = 0
    rh: int = M


def find_bridges(em: list[Node], m: int):
    bridges = [False] * m
    dfs(em)
    for node in em:
        for e in node.es.values():
            if node.h < em[e.end].h:
                bridges[e.i] = True

    return [i + 1 for i in range(len(bridges)) if bridges[i]]


def dfs(em: list[Node], i: int = 0, h: int = 0, visited=None):
    n = len(em)
    rh = M

    if visited is None:
        visited = [False] * n

    node = em[i]
    node.h = h
    visited[i] = True

    for e in node.es.values():
        if e.skip:
            continue
        em[e.end].es[e.i].skip = True
        if visited[e.end]:
            e.color = 1
            rh = min(node.h, em[e.end].h, rh)
            continue
        visited[e.end] = True
        e.color = 0
        rh = min(rh, dfs(em, e.end, h + 1, visited))

    node.h = rh
    return rh


n, m = map(int, input().split())

em = [Node() for _ in range(n)]

for i in range(m):
    a, b = map(lambda x: int(x) - 1, input().rstrip().split())
    e = Edge(b, 0, i)
    em[a].es[i] = e
    em[b].es[i] = e


res = find_bridges(em, m)
print(len(res))

for r in res:
    print(r)
