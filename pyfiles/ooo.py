lis=[]
def met(n):
    for i in range(1, n+1):
        if n%i==0:
            lis.append(i)
    return  sum(lis)

print(met(25))
