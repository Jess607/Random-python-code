lis=[10, 20, 20, 10, 10, 30, 50, 10, 20]


for i in range(len(lis)-1):
    for j in range(i+1, len(lis)):
        if lis[i]==lis[j]:
            lis[j]=None
print(lis[2])
n=27
count=0
while n%3==0:
    n=n/3
    count=count+1
print(count)
