
lis=[1,1]
les=[1]
def factor(arr,arrb):
    j=0
    lis=[]
    les=[]
    for i in range(1,min(arr)+1):
        if len(arr)==2:
            #if arr[j]%i!=0 or arr[j]%i==0 and arr[j+1]%i!=0:
                #break
            if arr[j]%i==0 and arr[j+1]%i==0:
                lis.append(i)
        if len(arr)>2:
            #if arr[j]%i!=0 or arr[j]%i==0 and arr[j+1]%i!=0:
                #break
             if arr[j]%i==0 and arr[j+1]%i==0 and arr[j+2]%i==0:
                 lis.append(i)

    if len(arrb)==1:
        for i in range(len(lis)):
            if lis[i]%arrb[0]==0:
                les.append(i)
        return len(les)
    if len(arrb)>1:
        for i in range(len(lis)):
            for a in range(len(arrb)-1):
                #if i%arrb[a]!=0 or i%arrb[a]==0 and i%arrb[a+1]!=0:
                        #break
                if lis[i]%arrb[a]==0 and lis[i]%arrb[a+1]==0:
                    les.append(lis[i])
        return les










print(factor(lis,les))
