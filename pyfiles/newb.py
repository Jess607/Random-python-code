def divisibleSumPairs(n, k, ar):
    count=0
    lis=[]
    for i in range(len(ar)):
        for j in range(1,len(ar)-i):
            if (ar[i] +ar[i+j])%k==0:
                count=count+1
    return count


print(divisibleSumPairs(6,5,[1,2,3,4,5,6]))
