def log(n):
    count=0
    while n//2!=1:
        n=n//2
        count=count+1
    return count

print(log(7))
