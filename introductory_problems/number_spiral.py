def f(a,b):M=max(a,b);print((a-b)*(-1)**M+M*M-M+1)

for i in range(int(input())):

    a,b=map(int, input().split())
    f(a,b)