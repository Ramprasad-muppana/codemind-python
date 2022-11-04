s=list(map(str,input().split()))
a='aeiou'
b=[]
c=0
for i in s:
    c=0
    i=i.lower()
    for j in i:
        if j in a:
            c=c+1
    print(c,end=' ')