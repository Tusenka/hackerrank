#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=32&id_topic=57&id_problem=1050
M=10**9

class State:
    def __init__(self, a: list[list[int]]):
        self.a=a
        n=len(a)
        self.min_rows = [M]*n
        self.min_cols = [M]*n
        self.covered_rows = [False]*n
        self.covered_cols= [False]*n
        self.marked_zeros = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            self.min_rows[i] = min(a[i])

        for j in range(n):
            self.min_cols[j] = min([a[i][j] for i in range(n)])

    def sub_row(self, i, delta):
        for j in range(len(self.a)):
            self.a[i][j]-=delta
            self.min_rows[i]-=delta

    def sub_col(self, j, delta):
        for i in range(len(self.a)):
            self.a[i][j]-=delta
            self.min_cols[j]-=delta

    def find_min_row(self, i):
        return self.min_rows[i]

    def find_min_col(self, j):
        return self.min_cols[j]

    def _reset(self):
        for i in range(len(self.a)):
            self.covered_cols[i]=False
            self.covered_rows[i]=False

    def _find_min(self):
        min_=M
        for i in range(len(self.a)):
            if not self.covered_rows[i]:
                for j in range(len(self.a)):
                    if not self.covered_cols[j]:
                        min_=min(min_,self.a[i][j])
        return min_


    def _cover_zeros(self):
        self._reset()

        for i in range(len(self.a)):
            for j in range(len(self.a)):
                if self.a[i][j]==0 and not self.covered_rows[i] and not self.covered_cols[j]:
                    self.marked_zeros[i][j]=1
                    self.covered_rows[i]=True
                    self.covered_cols[j]=True


        self._reset()

        for i in range(len(self.a)):
            if sum(self.marked_zeros[i])>0:
                continue

            for j in range(len(self.a)):
                if self.a[i][j]==0 and not self.covered_cols[j]:
                    self.covered_cols[j]=True
                    self.covered_rows[i]=True

        self.covered_rows=[not x for x in self.covered_rows]

    def _argument_path(self):
        delta=self._find_min()
        for i in range(len(self.a)):
            for j in range(len(self.a)):
                if self.covered_rows[i] and self.covered_cols[j]:
                    self.a[i][j]+=delta
                elif not self.covered_rows[i] and not self.covered_cols[j]:
                    self.a[i][j]-=delta

    def _check_solution(self):
        if sum(self.covered_rows)+sum(self.covered_cols)<len(self.a):
            return False, None

        ans={}
        return True




def solve(a: list[list[int]]):
    pass

n=int(input())

a=[[M for _ in range(n)] for _ in range(n)]

for i in range(n):
    a[i]=list(map(int, input().split()))


