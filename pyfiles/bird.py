#doc=input('Enter path:')
#with open(doc, 'r') as file:
#lis=list(abs)

def bird(arr):
    max=0
    for i in range(1,6):
        count=0
        for j in range(len(arr)):
            if i==arr[j]:
                count=count+1
            if count>max:
                max=count
                a=i
    return a
            #if count==max:
                #if i<a:
                    #a=i


print(bird([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
