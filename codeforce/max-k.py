# https://codeforces.com/edu/course/2/lesson/4/1/practice/status
from __future__ import annotations

import dataclasses
from typing import Annotated, Callable, Iterable


@dataclasses.dataclass
class TreeNode:
    f: Callable = sum
    val: int | None = None
    range: tuple[int, int] | None = None
    left: TreeNode | None = None
    right: TreeNode | None = None
    is_leaf: bool = False
    lmax_val = None
    rmax_val = None

    def load(self, a, i=0, j=-1):
        j = j if j >= 0 else len(a) - 1
        self.range = (i, j)

        if i == j:
            return self._load_leaf(a, i)

        self.left = TreeNode(f=self.f)
        self.right = TreeNode(f=self.f)
        self.left.load(a, i, (j + i) // 2)
        self.right.load(a, (i + j) // 2 + 1, j)

        self.rmax_val = max(
            self.right.rmax_val, self.f(self.left.rmax_val, self.right.rmax_val)
        )
        self.lmax_val = max(
            self.left.lmax_val, self.f(self.right.lmax_val, self.left.lmax_val)
        )

        self.val = self.f(self.left.val, self.right.val)

    def _load_leaf(self, a, i):
        self.val = a[i]
        self.range = (i, i)
        self.lmax_val = a[i]
        self.rmax_val = a[i]
        self.is_leaf = True

        return a[i]

    def _is_include(self, i):
        return self.range[0] <= i <= self.range[1]

    def _get_child(self, i) -> TreeNode:
        if self.is_leaf:
            return None

        if self.left._is_include(i):
            return self.left

        if self.right._is_include(i):
            return self.right

    def get_max(self):
        if self.is_leaf:
            return self.val
        return max(
            self.left.get_max(),
            self.right.get_max(),
            self.f(self.left.rmax_val, self.right.lmax_val),
        )

    def get_k(self, k: int):
        if self.is_leaf:
            return self if self.val == k else None
        if k == 0:
            return (
                self.left.get_k(k)
                if self.left.val < self.right.val
                else self.right.get_k(k)
            )
        else:
            return (
                self.left.get_k(k)
                if self.left.val > self.right.val
                else self.right.get_k(k)
            )

    def get(self, i, j):
        if self.is_leaf:
            return self.val

        if i <= self.range[0] and j >= self.range[1]:
            return self.val

        intl = self.left if self.left.range[1] >= i else self.right
        intr = self.left if self.right.range[0] > j else self.right

        return (
            intl.get(i, j) if intl == intr else self.f(intl.get(i, j), intr.get(i, j))
        )

    def update(self, i, v):
        if self.is_leaf:
            self.val = v
            self.lmax_val = v
            self.rmax_val = v
            return

        self._get_child(i).update(i, v)

        self.rmax_val = max(
            self.right.rmax_val, self.f(self.left.rmax_val, self.right.val)
        )
        self.lmax_val = max(
            self.left.lmax_val, self.f(self.left.val, self.right.lmax_val)
        )

        self.val = self.f(self.left.val, self.right.val)

    def revert(self, i):
        if self.is_leaf:
            self.val = self.val ^ 1
            self.lmax_val = self.val
            self.rmax_val = self.val
            return

        self._get_child(i).revert(i)

        self.rmax_val = max(
            self.right.rmax_val, self.f(self.left.rmax_val, self.right.val)
        )
        self.lmax_val = max(
            self.left.lmax_val, self.f(self.left.val, self.right.lmax_val)
        )

        self.val = self.f(self.left.val, self.right.val)


def _solve(a):
    pass


n, m = tuple(int(x) for x in input().rstrip().split())

a = tuple(int(x) for x in input().rstrip().split())
tree = TreeNode(f=lambda x, y: x + y)
tree.load(a)
for _ in range(m):
    o = tuple(int(x) for x in input().rstrip().split())

    if o[0] == 1:
        tree.update(o[1], o[2])
    else:
        print(tree.get_k(o[1]).range[0])
