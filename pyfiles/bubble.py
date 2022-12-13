arr=[3,2,1]
def sortd(arr):
    count=0
    while arr!= sorted(arr):
        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                arr[i]=arr[i]
            elif arr[i]>arr[i
            +1]:
                arr[i], arr[i+1]=arr[i+1], arr[i]
                count=count+1
    return arr[0], arr[-1], count



print(sortd(arr))
