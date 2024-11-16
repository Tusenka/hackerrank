#!/bin/python3

import os

def _iter_swap(m,i,j):
    for [x, y] in [(i,j), (len(m)-i-1, j), (i, len(m)-j-1), (len(m)-i-1, len(m)-j-1)]:
        yield m[x][y]
    

def _get_max(m, i, j):
    return max(_iter_swap(m, i, j))
 
    
def _iter_corner(m):
    for i in range(len(m) >> 1):
        for j in range(len(m) >> 1):
            yield i, j 
    return       
      
def flippingMatrix(matrix):
    return sum([_get_max(matrix, i, j) for [i,j] in _iter_corner(matrix)])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
