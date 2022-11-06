def prime(a):
    for i in range(2,(a//2)+1):
        if a%i==0:
            return(0)
    else:
        return(1)
a=input()
b=a[::-1]
a=int(a)
b=int(b)
p=prime(a)
q=prime(b)
if p+q==2:
    print("circular prime")
elif p==1:
    print("prime but not a circular prime")
else:
    print("not prime")    