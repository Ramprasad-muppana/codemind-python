p=int(input())
q=int(input())
c=[]
for a in range(p,q+1):
    a=list(str(a))
    b=int(''.join(a))
    for i in a:
        try:
            if b%int(i)!=0:
                break
        except:
            break
    else:
        c.append(b)    
print(*c,sep=' ')