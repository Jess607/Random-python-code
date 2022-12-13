def reo(arr):
    count=0
    lis=[len(arr)]
    for i in sorted(list(set(arr))):
        for j in range(len(arr)):
            if arr[j]==i:
                count=count+1
        min=len(arr)-count
        lis.append(min)
    lis.pop(-1)
    return lis

print(reo([1,2,3]))
