a=input()
if int(a)>=0:
    print(int(a[::-1]))
else:
    a=a[1:]
    print('-',end='')
    print(int(a[::-1]))