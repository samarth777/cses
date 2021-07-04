n=int(input())

c=0
s=5

while (n//s)>0:
    c+=(n//s)
    s=s*5
print(c)

