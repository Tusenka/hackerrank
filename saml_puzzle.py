#!/bin/python3

import math
import os
import random
import re
import sys
from dataclasses import dataclass
from functools import reduce
import itertools


@dataclass
class Step:
    i: int
    j: int
    k: int
    score: int
    m: list[list[int]]
        
    
_g_cache={}
        
def _print_matrix(m):
    for x in m:
        print(' '.join([str(v) for v in x]))

def _get_matrix_hash(m):
    global _g_cache
    _hash=0
    for x in m:
        _hash+=hash(tuple(x))
    return _hash


def _rotate_layer(m, i, j, k):
    if k==1:
        return m
    ulcorn=m[i][j]
    urcorn=m[i][j+k-1]
    dlcorn=m[i+k-1][j]
    drcorn=m[i+k-1][j+k-1]
    if k==2:
        m[i][j]=dlcorn
        m[i][j+1]=ulcorn
        m[i+1][j+1]=urcorn
        m[i+1][j]=drcorn
        return m
    #rows
    for x in reversed(range(j+1, j+k)):
        m[i][x]=m[i][x-1]
    
    for x in range(j, j+k-1):
        m[i+k-1][x]=m[i+k-1][x+1]
    
    #cols    
    for x in reversed(range(i+1, i+k)):
        m[x][j+k-1]=m[x-1][j+k-1]
    for x in range(i, i+k-1):
        m[x][j]=m[x+1][j]
    
    #corners     
    m[i][j+1]=ulcorn
    m[i+1][j+k-1]=urcorn
    m[i+k-1][j+k-2]=drcorn
    m[i+k-2][j]=dlcorn 
        
def _rotate(m, i, j, k):
    x, y=i, j
    while k>1:
        _rotate_layer(m, x, y, k)
        x+=1
        y+-1
        k-=1
    
    
def _goodness(m):
    res=0
    key=_get_matrix_hash(m)
    if key in _g_cache:
        return _g_cache[key]
    for x in range(len(m)):
        for j1 in range(0, len(m)-1):
           for j2 in range(j1+1, len(m)):
               if m[x][j1]<m[x][j2]:
                   res+=1
               if m[j1][x]<m[j2][x]:
                   res+=1 
    _g_cache[key]=res                                              
    return res
    
            
def _possible_rotations(m):
    for i in range(len(m)):
        for j in range(len(m)):
            for k in range(2, len(m)-max(i,j)+1):
                 yield Step(i, j, k, None, None)
        
            
def _get_next_step_chain(m,  depth, gmax):
    possible_rotations=list(_possible_rotations(m))
    chains=itertools.product(possible_rotations, repeat=depth)
    best_step_g=0
    best_step=0
    best_chain_g=0
    best_chain=[]
    for chain in chains:
        m1=[row[:] for row in m]
        for j, step in enumerate(chain):
            _rotate(m1, step.i, step.j, step.k)
            step.m=m1
            step.score=_goodness(m1)
            if best_step_g<step.score:
                best_step_g=step.score
                best_step=j
            # stop when maximum archived
            if best_step_g==gmax: break
            
        if best_chain_g<best_step_g:
            best_chain=chain
            best_chain_g=best_step_g
        # stop when maximum archived
        if best_chain_g==gmax: break
    return list(best_chain[:best_step+1])        
            


def _try_random_rotation(m):
     return random.choice(list(_possible_rotations(m)))
    
def get_next_steps(m,):
    gmax=(len(m)**2) *(len(m)-1)
    gcurrent=_goodness(m)
    steps=[]
    while gcurrent<gmax and len(steps)<500:
        step_chain=_get_next_step_chain(m, 4, gmax)
        if gcurrent<=step_chain[-1].score:
            for _ in range(random.randint(0,5)):
                steps.append(_try_random_rotation(m))
        else:
            gcurrent=step_chain[-1].score
            steps=steps+step_chain
    print(len(steps))  
    for step in steps:    
        print(step.i+1, step.j+1, step.k)

    
if __name__ == '__main__':
    n = int(input().strip())

    puzzle = []

    for _ in range(n):
        puzzle.append(list(map(int, input().rstrip().split())))

    get_next_steps(puzzle)

    # Write your code here
