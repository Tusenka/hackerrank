#https://teach-in.ru/lecture/04-15-Serdobolskaya

import dataclasses
import itertools
import sys
from collections import deque
from copy import deepcopy

M=10**9
@dataclasses.dataclass
class State:
    x:tuple[int, int]
    pos: list[list]

    def swaps(self):
        steps=[]
        i,j=self.x
        if i<1: steps.append((i+1,j))
        if j<3: steps.append((i,j+1))
        if i>0: steps.append((i-1,j))
        if j>0: steps.append((i,j-1))
        for step in steps:
            pos=deepcopy(self.pos)
            pos[i][j], pos[step[0]][step[1]]=pos[step[0]][step[1]], pos[i][j]
            yield State(x=step, pos=pos)

    def __eq__(self, other):
        return self.__hash__()==other.__hash__()

    def __hash__(self):
        return hash(tuple(tuple(i) for i in self.pos))

def _bfs(x: State, y: State):
    d = {x: 0}
    queue = deque([x])

    while queue:
        state = queue.popleft()
        for step in state.swaps():
            if step not in d:
                queue.append(step)
                d[step] = d[state] + 1
                if step == y:
                    return d[step]

    return -1

def _get_state(a):
    for i, j in itertools.product(range(len(a)), range(len(a[0]))):
        if a[i][j] == '#':
            return State((i, j), a)

def _get_array():
    return list(input().rstrip())


if __name__ == '__main__':
    sys.setrecursionlimit(100009)
    n, m = 2, 4
    a = [_get_array(), _get_array()]
    b = [_get_array(), _get_array()]
    x=_get_state(a)
    y=_get_state(b)

    print(_bfs(x, y))

