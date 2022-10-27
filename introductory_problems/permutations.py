n=int(input())
le=[]
lo=[]
if n==1:
    print(1)
elif n<=3:
    print('NO SOLUTION')
else:
    for i in range(1, n+1):
        if i%2==0:
            le.append(i)
        else:
            lo.append(i)
print(*le+lo)