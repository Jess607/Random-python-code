def jump(arr):
    max=0
    for i in (list(set(arr))):
        if arr.count(i)>max:
            max=arr.count(i)
    ans=len(arr)-max
    return ans


print(jump([1,2,2,3]))
