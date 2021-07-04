s=list(input())
d=dict()
print(s)
for i in s:
    if i not in d:
        d[i]=s.count(i)
print(d)
c=0
for i in d.values():
    if i%2!=0:
        c+=1
cnt=0
s=[]
if c>1:
    print('NO SOLUTION')
else:
    for i in d.keys():
        if d[i]%2!=0:
            cnt=i
        s+=i*(d[i]2)
print(s)