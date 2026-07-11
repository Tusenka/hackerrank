from __future__ import annotations
import dataclasses
import random
from dataclasses import field

M=10**9

@dataclasses.dataclass
class Node:
    next: Node|None = None
    hash: int =field(default_factory= lambda : random.randint(1, M))

def solve(start: Node):
    step=1
    last=start
    x=start

    while True:
        next_point=step*2+step
        for _ in range(step*2):
            

def check_cyclic(cur: Node) -> bool:
    slow=start
    fast=start

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

        if slow==fast:
            return True

    return False