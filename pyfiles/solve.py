lis=[1,1,2,2,4,4,5,5,5]

def solve(arr):
    arr=sorted(arr)
    a=0
    for i in range(len(arr)):
        l=1
        for n in range(i+1, len(arr)):
            if abs(arr[i]-arr[n])<=1:
                l=l+1
        if l>a:
            a=l
    return a


print(solve(lis))
