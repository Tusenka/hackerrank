from __future__ import annotations
import dataclasses

M = 10**9


@dataclasses.dataclass
class TreeNode:
    left_child: TreeNode | None = None
    right_child: TreeNode | None = None
    added_value: int | None = 0
    min_value: int | None = 0
    range: tuple[int, int] | None = None

    is_leaf = False

    def load(self, a: list, i=0, j=-1):
        if j == -1:
            j = len(a) - 1

        self.range = (i, j)
        if i == j:
            self.is_leaf = True
            self.added_value = a[i]
            return

        self.left_child = TreeNode()
        self.right_child = TreeNode()
        self.left_child.load(a=a, i=i, j=(i + j) // 2)
        self.right_child.load(a=a, i=(i + j) // 2 + 1, j=j)
        self.min_value = min(self.left_child.min_value, self.right_child.min_value)

    def find_min(self, l: int, r: int):
        if not self._in_range(l, r):
            return M

        if self.is_leaf:
            return self.min_value + self.added_value

        if self.left_child._in_range(l, r) and self.right_child._in_range(l, r):
            return (
                min(self.left_child.find_min(l, r), self.right_child.find_min(l, r))
                + self.added_value
            )

        if self.left_child._in_range(l, r):
            return self.left_child.find_min(l, r) + self.added_value

        if self.right_child._in_range(l, r):
            return self.right_child.find_min(l, r) + self.added_value

        return None

    def add_value(self, v: int, l: int, r: int):
        if not self._in_range(l, r):
            return

        if self.is_leaf:
            self.added_value += v
            # print(self.range, "leaf")
            return

        if self._is_covered_by_range(i=l, j=r):
            # print(self.range, "covered")
            self.added_value += v
            return

        if self.left_child._in_range(l, r):
            # print(self.range, "left")
            self.left_child.add_value(v, l, r)

        if self.right_child._in_range(l, r):
            # print(self.range, "right")
            self.right_child.add_value(v, l, r)

    def _in_range(self, i, j):
        return (
            self.range[0] <= i <= self.range[1] or self.range[0] <= j <= self.range[1]
        )

    def _is_covered_by_range(self, i, j):
        return i <= self.range[0] and j >= self.range[1]


n, t = tuple(map(int, input().split()))
stree = TreeNode()
stree.load([0] * (n + 1))

for i in range(t):
    o = tuple(map(int, input().split()))
    if o[0] == 1:
        stree.add_value(v=o[3], l=o[1], r=o[2])
    else:
        print(stree.find_min(l=o[1], r=o[2]))
