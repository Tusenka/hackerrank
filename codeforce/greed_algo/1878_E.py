import dataclasses


@dataclasses.dataclass
class Tree:
    btree: list[int] | None=None
    n: int=0
    def load(self, a: list, i=0, begin:int=0, end:int=-1):
        self.n=len(a)

        end = len(a) - 1 if end == -1 else end
        if self.btree is None:
            n = (len(a)) * 4
            self.btree= [-1] *  n
        if begin == end:
            self.btree[i] = a[begin]
            return

        l = i * 2 + 1
        r = i * 2 + 2
        m = (begin + end) // 2
        self.load(a, l, begin, m)
        self.load(a, r, m + 1, end)

        self.btree[i] = self.btree[l]&self.btree[r]

    def get_value(self, l,r):
        return self._get_value(l=l, r=r, idx=0, begin=0, end=len(self.btree) // 4 - 1)

    def _get_value(self, l, r, idx, begin, end)->int:
        if begin > r or end < l:
            return -1

        if begin == end:
            return self.btree[idx]

        if begin == l and r == end:
            return self.btree[idx]

        m = (begin + end) // 2
        return self._get_value( l=l, r=r, idx=idx * 2 + 1, begin=begin, end=m)&self._get_value( l, r, idx * 2 + 2, m + 1, end)

def  solve(tree: Tree, l, k):
     _cache={}
     for x in range(tree.n-1, l-1, -1):
         if tree.get_value(l=l,r=x)>=k:
            return x+1

     return -1

t=int(input())

for _ in range(t):
    _=input()
    a=list(map(int, input().split()))
    tree=Tree()
    tree.load(a=a)

    q=int(input())
    ans=[-1]*q
    for i in range(q):
        l,k=tuple(map(int, input().split()))
        ans[i]=solve(tree, l=l-1, k=k)

    print(*ans)