n=int(input())
a=[]
for i in range(2,n//2+1):
    c=[]
    k=[]
    if n%i==0:
        c.extend([i,n//i])
        for p in c:
            for j in range(2,p//2+1):
                if p%j==0:
                    break
            else:
                k.append(p)
        if len(k)==2:
            a.extend(k)
if len(a)>0:
    print(a[0],a[1])
else:
    print(-1)