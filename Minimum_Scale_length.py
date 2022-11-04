n=int(input())
l=list(map(int,input().split()))
a=min(l)
for i in range(a,0,-1):
    for j in l:
        if j%i!=0:
            break
    else:
        print(i)
        break