n=int(input('Enter:'))
lis=[]
les=[]
ls=[]
k=5
for i in range(1, n+1):
    lis.append(i)
x=len(lis)
for a in range(0, len(lis)):
    for b in range(1, x):
        les.append((lis[a] & lis[a+b]))
    x=x-1
for i in les:
    if i<k:
        ls.append(i)
print(max(ls))
