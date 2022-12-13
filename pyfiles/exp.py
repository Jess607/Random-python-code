lis=[20,30,12]

def exp(arr):
    j=0
    lis=[]
    for i in range(1,8):
        while j<len(arr)-1:
            if arr[j]%i==0 and arr[j+1]%i==0:
                    lis.append(i)
            j=j+1
    print(lis)

print(exp(lis))
