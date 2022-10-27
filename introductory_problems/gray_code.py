n=int(input())
l=[]
for i in range(2**n):
    l.append(bin(i)[2:])

m=0
for i in l:
    if len(i)>m:
        m=len(i)
    else:
        continue

for i in l:
    if len(i)<m:
        print((m-len(i))*'0'+i)
    else:
        print(i)