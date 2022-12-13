S='adbecf'
lis=[]
les=[]
for i in S:
    if (S.index(i))%2==0:
        lis.append(i)
s=''.join(lis)
for j in S:
    if (S.index(j))%2!=0:
        les.append(j)
a=''.join(les)
print(s + '  ' + a )
