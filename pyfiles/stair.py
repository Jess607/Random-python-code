arr=[1,2,3,4,5]
def ste(arr):
    i=0
    lis=[]
    for i in range(len(arr)):
        tot=sum(arr)-arr[i]
        lis.append(tot)
    return max(lis), min(lis)

print(ste(arr))
