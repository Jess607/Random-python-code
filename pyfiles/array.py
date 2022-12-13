if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    res=arr[::-1]
    b=''
    for i in res:
        print(i,'', end='')
