n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if(i&1 and i not in c):
        c.append(i)
print(len(c))        