lis=[10, 20, 20, 10, 10, 30, 50, 10, 20]

def socks(arr):
    lis=[]
    count_a=0
    for i in range(len(arr)):
        if arr[i] not in lis:
            lis.append(arr[i])
    for j in range(len(lis)):
        count=0
        for a in range(len(arr)):
            if lis[j]==arr[a]:
                count=count+1
        count=count//2
        count_a =count_a + count
    return count_a





print(socks(lis))
