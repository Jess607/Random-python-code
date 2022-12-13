import numpy as np
lis=np.array([2,3,5,6,6])
lis.sort()
les=[]
for i in lis:
    if i not in les:
        les.append(i)
print(les[-2])
