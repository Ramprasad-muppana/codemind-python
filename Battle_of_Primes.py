def prime(a):
    for i in range(2,(a//2)+1):
        if a%i==0:
            return(0)
    else:
        return(1)
a=int(input())
b=int(input())
k=a+b+1
c=0
while(True):
    c=prime(k)
    if c==1:
        break
    k=k+1
print(k-(a+b))