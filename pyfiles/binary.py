n=int(input('Enter:'))
lis=[]
lis.append(n%2)
i=n//2
lis.append(i%2)
while i!=0:
    i=i//2
    lis.append(i%2)
a,res=0,0
for i in range(0, len(lis)):
    if lis[i]==0:
        a=0
    else:
        a+=1
        res=max(res,a)
print(res)
