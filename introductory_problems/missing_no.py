n=int(input())
l=list(map(int, input().split()))
s=sum(l)
print(int(((n*(n+1))/2)-s))