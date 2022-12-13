d=[1,2,3,4,5]

def rot(arr,n):
    for a in range(n):
        j=1
        for i in range(len(arr)-1):
            arr[i], arr[i+j]=arr[i+j], arr[i]
    return arr



print(rot(d,2))
