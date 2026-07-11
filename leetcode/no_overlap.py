from typing import NamedTuple

class Event(NamedTuple):
    x: int
    type: int #0 start, 1 -end
    val:int
    i: int


def solve(events:list[list[int]]):
    h=[]
    ans=0

    for i, x in enumerate(events):
        h.append(Event(x[0], 0, x[2], i))
        h.append(Event(x[1], 1, x[2], i))

    h.sort()
    closed=0
    for x in h:
         if x.type==1:
            closed=max(closed, x.val)
         else:
            ans=max(ans, closed+x.val)

    return ans