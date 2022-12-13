lis=[[11,2,4], [4,5,6], [10,8,-12]]

def jam(arr):
    tot=0
    j=0
    for i in range(len(arr)):
            tot=tot+ lis[i][j]
            j=j+1
            print(tot)
    tat=0
    j=-1
    for i in range(len(arr)):
        tat=tat + arr[i][j]
        j=j-1
        print(tat)




print(jam(lis))
