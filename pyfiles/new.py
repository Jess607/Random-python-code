lis=[45,87,75,96]


def gra(grades):
    # Write your code here
    lis=[]
    for i in range(0, len(grades)):
        if grades[i]<40:
            grade=grades[i]
        elif grades[i]>40:
            if grades[i]%5==0:
                grade= grades[i]+5
            elif grades[i]%5!=0:
                for a in range(grades[i], grades[i]+6):
                    if a%5==0:
                        diff=a-grades[i]
                        if diff<3:
                            grade=a
                        else:
                            grade=grades[i]
        lis.append(grade)
    return lis



print(gra(lis))
