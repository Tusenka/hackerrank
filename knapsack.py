import dataclasses


@dataclasses.dataclass
class Node:
    p: int
    w: int
def knapsack(a: list[Node], W):
    res=[0]*(W+1)
    for i in range(len(a)):
        for j in (W, a[i].w-1, -1):
            res[j]=max(res[j], res[j-a[i].w]+a[i].p)
    return res[W]
