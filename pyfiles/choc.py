lis=[3, 5, 4, 1, 2, 5, 3, 4, 3, 2, 1, 1, 2, 4, 2, 3, 4, 5, 3, 1, 2, 5, 4, 5, 4, 1, 1, 5, 3, 1, 4, 5, 2, 3, 2, 5, 2, 5, 2, 2, 1, 5, 3, 2, 5, 1, 2, 4, 3, 1, 5, 1, 3, 3, 5]
def choc(s,d,m):
    count=0
    if m==1:
        for n in range(len(s)):
            a=s[n]
        if a==d:
            count=count+1
    if m>1:
        y=m-1
        for n in range(len(s)-y):
            a=s[n]
            for i in range(1,m):
                a=a + s[n+i]
            print(a)
            if a==d:
                count=count+1
    return count



print(choc(lis,18,6))
