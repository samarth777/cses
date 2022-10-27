n=int(input())
arr=list(map(int, (input().split())))
c=0
for i in range(n-1):
    if arr[i]<=arr[i+1]:
        continue
    else:
        c+=(arr[i]-arr[i+1])
        arr[i+1]=arr[i]
    
print(c)