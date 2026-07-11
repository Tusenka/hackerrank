from __future__ import annotations

import dataclasses
from typing import Annotated, Callable, Iterable


@dataclasses.dataclass
class TreeNode:
    f: Callable
    val: int | None = None
    range: tuple[int, int] | None = None
    left: TreeNode | None = None
    right: TreeNode | None = None
    is_leaf = False

    def load(self, a, i = 0, j = -1):
        j = j if j >= 0 else len(a) - 1
        self.range = (i, j)

        if i == j:
            self.val = a[i]
            self.range = (i, i)
            self.is_leaf = True
            return a[i]

        self.left = TreeNode(f=self.f)
        self.right = TreeNode(f=self.f)
        self.left.load(a, i, (j + i) // 2)
        self.right.load(a, (i + j) // 2 + 1, j)
        self.val = self.f(self.left.val, self.right.val)

    def _is_include(self, i):
        return self.range[0] <= i <= self.range[1]

    def  get_max(self) -> TreeNode :
        if self.is_leaf:
            return self

        l = self.left.get_max()
        r = self.right.get_max()

        if l._is_adjusted(r):
            v
        v=self.f(l,r) if l._is_adjusted(r) else max(l.val, r.val)

        return TreeNode(f=self.f, right=r, left=l, v)

    def _is_adjusted(self, other: TreeNode):
        if self.range[1]==other.range[0]-1:
            return True
        if self.range[0]==other.range[1]+1:
            return True

        return False

    def _get_child(self, i) -> TreeNode:
        if self.is_leaf:
            return None

        if self.left._is_include(i):
            return self.left

        if self.right._is_include(i):
            return self.right

        return None

    def get(self, i, j):
        if self.is_leaf:
            return self.val

        if i <= self.range[0] and j >= self.range[1]:
            return self.val

        intl = self.left if self.left.range[1] >= i else self.right
        intr = self.left if self.right.range[0] > j else self.right

        return intl.get(i, j) if intl == intr else self.f(intl.get(i, j), intr.get(i, j))

    def update(self, i, v):
        if self.is_leaf:
            self.val = v
            return

        self._get_child(i).update(i, v)
        self.val = self.f(self.left.val, self.right.val)


def _solve(a):
    pass


n, m = tuple(int(x) for x in input().rstrip().split())

a = tuple(int(x) for x in input().rstrip().split())
tree = TreeNode(f=lambda x, y: x + y)
tree.load(a)
print(max(tree.get_max(),0))

for _ in range(m):
    i, j = tuple(int(x) for x in input().rstrip().split())
    tree.update(i, j)
    print(max(tree.get_max(),0))
