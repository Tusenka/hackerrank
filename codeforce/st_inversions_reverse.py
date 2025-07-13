# https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/B
from __future__ import annotations

import dataclasses
from typing import Annotated, Callable, Iterable


@dataclasses.dataclass
class TreeNode:
    f: Callable = max
    val: int | None = None
    range: tuple[int, int] | None = None
    left: TreeNode | None = None
    right: TreeNode | None = None
    is_leaf: bool = False

    def load(self, i, j):
        j = j if j >= 0 else len(a) - 1
        self.range = (i, j)

        if i == j:
            self._load_leaf(i)
            return

        self.left = TreeNode(f=self.f)
        self.right = TreeNode(f=self.f)
        self.left.load(i, (j + i) // 2)
        self.right.load((i + j) // 2 + 1, j)

        self.val = self.right.val+self.left.val

    def _load_leaf(self, i):
        self.val = 1
        self.range = (i, i)
        self.is_leaf = True


    def _is_include(self, i):
        return self.range[0] <= i <= self.range[1]

    def _get_child(self, i) -> TreeNode:
        if self.is_leaf:
            return None

        if self.left._is_include(i):
            return self.left

        if self.right._is_include(i):
            return self.right

    def build_reverse(self, a: tuple):
        res = [0] * len(a)

        for i in range(len(a)-1, -1, -1):
            j = self.get_k(a[i]+1)
            res[i]=j
            self.update(j, 0)

        return res

    def get_k(self, k):
        if self.is_leaf:
            return self.range[1]

        if self.right.val<k:
           return self.left.get_k(k-self.right.val)

        if self.right.val>=k:
            return self.right.get_k(k)


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

    def revert(self, i):
        if self.is_leaf:
            self.val = self.val ^ 1
            return

        self._get_child(i).revert(i)

        self.val = self.f(self.left.val, self.right.val)


def _solve(a):
    pass


n = int(input())

a = tuple(int(x) for x in input().rstrip().split())
tree = TreeNode(lambda x, y: x + y)
tree.load(0, n-1)
print(*[x+1 for x in tree.build_reverse(a)])
