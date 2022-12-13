lis=[1,2,3,4,5]
for j in range(2):
    for i in range(1, (len(lis))):
        lis[0], lis[i] = lis[i], lis [0]
print(lis)
