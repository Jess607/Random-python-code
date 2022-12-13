lis=[[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
i=0
j=0
les=[]
for i in range(len(lis)-2):
    for j in range(len(lis)-2):
        les.append(lis[i][j] + l
        is[i][j+1] + lis[i][j+2]+ lis[i+1][j+1]+ lis[i+2][j] + lis[i+2][j+1] + lis[i+2][j+2])
print(les)
