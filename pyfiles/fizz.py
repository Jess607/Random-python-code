def fizz(N):
    for i in range(1,N):
        num=i
        if i%3==0 and i%5!=0:
            num='fizz'
        if i%3!=0 and i%5==0:
            num='buzz'
        if i%3==0 and i%5==0:
            num='yeah'
        print(num)


print(fizz(35))
