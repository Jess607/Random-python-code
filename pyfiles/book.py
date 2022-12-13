def book(n,p):
    count=0
    count_a=0
    if p%2==0:
        for i in range(0, p, 2):
            count=count+1
        if n%2==0:
            for j in range(n, p, -2):
                count_a=count_a +1
        if n%2!=0:
            for j in range(n-1, p, -2):
                count_a=count_a +1
    if p%2!=0:
        for i in range(1, p, 2):
            count=count+1
        if n%2==0:
            for j in range(n+1, p, -2):
                count_a=count_a +1
        if n%2!=0:
            for j in range(n, p, -2):
                count_a=count_a +1

    return min(count, count_a)


print(book(10,3))
