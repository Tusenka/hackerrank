def floyd_warshall(arr : list[list[int]]):
    res=[]
    for x in arr:
        res.append([ v>0 for v in x ] )
    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                res[i][j]=(res[i][k] and res[k][j]) or res[i][j]
    return res

graph = [[1, 1, 0, 1],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [0, 0, 0, 1]]

print(floyd_warshall(graph))