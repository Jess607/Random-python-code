import re
n=int(input())
lis=[]
for i in range(0,n):
    s=input()
    lis.append(s)
total=[]
total_2=[]
def regex(txt):
    match=re.findall('\D+', txt)
    return match
def reg(txt):
    match=re.findall('\d+', txt)
    return match

result=list(map(regex, lis))
result_2=list(map(reg, lis))

for i in range(0, len(result)):
    total.append(result[i][0])
#print(total)

for i in range(0, len(result_2)):
    total_2.append(result_2[i][0])

def keysd(hor, k):
    if k in hor.keys():
        print(k, '=', hor[k])
    else:
        print('Not found')

keysd(res_dict, )
#dict={}
#for (i,j) in zip(result, result_2):
    #print(i)
