a=int(input())
b=int(input())
c=max(a,b)
a1=[]
b1=[]
for i in range(1,(c//2)+1):
    if a%i==0:
        a1.append(i)
    if b%i==0:
        b1.append(i)
if sum(a1)==b and sum(b1)==a:
    print("Amicable")
else:
    print("Not Amicable")