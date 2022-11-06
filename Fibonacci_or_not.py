n=int(input())
a=0
b=1
d=[a,b]
for i in range(2,50):
    c=a+b
    a,b=b,c
    d.append(c)
if(n in d):
    print(True)
else:
    print(False)