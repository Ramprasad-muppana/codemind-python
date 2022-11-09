n=int(input())
b=int(input())
a=[]
k=0
while(n>0):
    c=n%b
    n=n//b
    if c==0:
        k=k+1
    else:
        a.append(k)
        k=0
if max(a)==0:
    print(-1)
else:    
    print(max(a))        
        
    
    
    