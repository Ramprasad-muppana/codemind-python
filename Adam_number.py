a=input()
b=a[::-1]
a1=int(a)
b1=int(b)
a1=a1**2
b1=b1**2
b1=str(b1)
b1=b1[::-1]
a1=str(a1)
if a1==b1:
    print("True")
else:
    print("False")