a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=[]
for i in l1:
    if i not in l2 and i not in c:
        c.append(i)
        print(i,end=' ')
for i in l2:
    if i not in l1 and i not in c:
        c.append(i)
        print(i,end=' ')        