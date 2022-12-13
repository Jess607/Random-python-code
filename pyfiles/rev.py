
count=0
shared=5
for i in range(3):
    liked=shared//2
    count=count + liked
    shared = liked * 3
print(count)
