n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(0,n//2):
    print(l[i],l[-(i+1)],end=' ')
if len(l)%2!=0:
    print(l[n//2],0)
    