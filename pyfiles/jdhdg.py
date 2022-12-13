les=[]
for i in range(3):
    name = input('Enter:')
    score = float(input('Enter:'))
    lis=[]
    lis.append(name)
    lis.append(score)
    #print(lis)
    les.append(lis)

grades=sorted(set(g for _, g in les))
second=grades[1]
for name in sorted(n for n,g in les if g==second):
    print(name)

#for name in sorted(n for n,g in les if g==findLargest())
