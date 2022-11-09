n=int(input())
c=2
a=0
b=1
print(a,b,end=' ')
while(c<n):
  print(a+b,end=' ')
  a,b=b,a+b
  c=c+1