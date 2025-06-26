#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=21&id_topic=51&id_problem=654

import sys
M=10**9
def _min_path(x, y):
    m=4
    d = {x: 0}
    queue = [x]
    p = {x: None }
    while queue:
        state=queue.pop(0)
        steps=[]
        if int(state[0])<9:
            steps.append(_set(state, 0, str(int(state[0])+1)))
        if int(state[-1])>1:
            steps.append(_set(state, 3, str(int(state[-1])-1)))
        steps.extend((_swap_l(state), _swap_r(state)))
        for step in steps:
            _mark_queue(queue=queue, step=step, o=state,  d=d, p=p )
            if step==y:
                break
    return p

def _set(s, i, c):
    return s[:i] + c + s[i+1:]

def _swap_r(s):
    return s[1:]+s[0]

def _swap_l(s):
    return s[-1]+s[:-1]

def _mark_queue(queue, step, o, d, p):
    if step not in d:
        queue.append(step)
        d[step]= d[o]+1
        p[step]= o


if __name__ == '__main__':
    sys.setrecursionlimit(100009)
    x=input().rstrip()
    y=input().rstrip()
    p=_min_path(x, y)
    q=[y]
    e=y
    while e:=p[e]:
        q.insert(0, e)
    for x in q:
        print(x)
