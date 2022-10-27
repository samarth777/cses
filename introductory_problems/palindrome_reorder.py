s=list(input())
d=dict()
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
c=0
for i in d.values():
    if i == 1:
        c+=1
l=[]
if c==1:
    for i in d.keys():
        if d[i]!=1:
            l.append(i*int(d[i]/2))
        else:
            odd=i
    l.append(odd)
else:
    print('NO SOLUTION')

print(l)