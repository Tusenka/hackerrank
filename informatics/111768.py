from __future__ import annotations
M=3000

class Tree:
    left: Tree | None= None
    right: Tree | None =None
    min_val: int | 0 = 0
    max_val: int | 0 = 0
    ad: int | 0 =0
    start: int=0
    end: int=-1

    def __init__(self, start: int, end: int):
        self.start=start
        self.end=end
        if start==end:
           return

        self.left=Tree(start=start, end=(end+start)//2)
        self.right=Tree(start=(end+start)//2+1, end=end)

    def add_vals(self, i, j, val=1):
        if self.start>j or self.end<i:
           return

        if self.start==self.end:
           self.min_val+=val
           self.max_val+=val
           return

        if self.start>=i and self.end<=j:
           self.ad+=val
        else:
           self.left.add_vals(i,j, val=val)
           self.right.add_vals(i, j, val=val)
        if self.left.ad>0 or self.right.ad>0 and self.ad>0:
           self.left.ad+=self.ad
           self.right.ad+=self.ad
           self.ad=0


        self.min_val= min(self.right.min_val+self.right.ad, self.left.min_val+self.left.ad)
        self.max_val= max(self.right.max_val+self.right.ad, self.left.max_val+self.left.ad)

    def get_min(self, i: int, j: int):
        if self.start>j or self.end<i:
           return M

        if self.start==self.end:
            return self.min_val+self.ad
        if self.start>=i and self.end<=j:
            return self.min_val+self.ad

        return min(self.left.get_min(i,j), self.right.get_min(i, j))+self.ad

    def assert_integrity(self, i, j):
        return self.get_min(i, j)==1



def solve(a: list[int]):
    tree=Tree(start=0, end=9999)
    events=[-1]*len(a)
    for i in range(0, len(a), 2):
        tree.add_vals(a[i], a[i+1]- 1, 1)
        events[i]=a[i]
        events[i+1]=a[i+1]

    events.sort()
    for i in range(1, len(events)):
        if not tree.assert_integrity(i=events[i-1], j=events[i]):
            return False

    return tree.assert_integrity(i=0, j=len(a)//2)




t=int(input())

for _ in range(t):
    a=list(map(int, input().split()))
    print("Accepted" if solve(a[1:]) else "Wrong Answer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ")