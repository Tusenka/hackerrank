from typing import NamedTuple, cast

class Point(NamedTuple):
      x: int
      y: int


class Rect(NamedTuple):
    start: Point
    end: Point

    def get_area(self):
        return (self.end.x-self.start.x)*(self.end.y-self.start.y)


class Line(NamedTuple):
      start: int
      end: int
      i: int
      actual_start: int
      enabled:bool=True

def add_segments(sa: list[Line], s:Line, val:int):
    import bisect

    idx=bisect.bisect_left(sa, s)
    i=idx

    if len(sa)<1 or idx==len(sa)-1 or sa[i-1].start>s.end:
        sa.insert(idx, s)

        return val+s.end-s.start, idx

    actual_start=s.start
    end=s.end

    while i<len(sa) and sa[i].start<=s.end:
        if sa[i].start==s.start and sa[i].end==s.end:
            i+=1
            break

        actual_start=max(actual_start,sa[i].end)
        end=max(actual_start,end)

        if s.end==s.start:
           break

        i+=1

    s=s._replace(actual_start=actual_start)

    sa.insert(idx, s)

    return (val+end-s.actual_start), idx

class Event(NamedTuple):
    x: int
    type: int
    i: int

def get_h(a: list[Rect], active: set[int]):

    if not active:
        return 0
    al=sorted([(a[i].start.y, a[i].end.y) for i in active])

    h=0
    start=al[0][0]
    end=al[0][1]
    for x in al:
        if x[0]<=end:
           end=max(end, x[1])
        if x[0]>=end:
           h+=end-start
           start=x[0]
           end=x[1]

    return h+end-start


def solve(a: list[Rect]):
    event=[]
    ans=0
    for i, point in enumerate(a):
        if not (point.start.x-point.end.x) or not (point.start.y-point.end.y):
            continue

        event.append(Event(point.start.x, 0, i))
        event.append(Event(point.end.x, 1, i))

    event.sort()

    active=set()
    last=0
    ans=0
    for e in event:
        e=cast(Event, e)
        h=get_h(a=a, active=active)
        if e.type==0:
            active.add(e.i)
        else:
            active.remove(e.i)

        ans+=h*(e.x-last)
        last=e.x

    return ans



n=int(input())
a=[Rect(Point(0,0),Point(0,0))]*n

for i in range(n):
    raw=tuple(map(int, input().split()))

    a[i]=Rect(start=Point(raw[0], raw[1]), end=Point(raw[2], raw[3]))


print(solve(a=a))

