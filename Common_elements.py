a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=[]
for i in l1:
    if i in l2 and i not in c:
        c.append(i)
        print(i,end=' ')