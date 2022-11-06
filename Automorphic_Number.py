n=int(input())
n1=str(n*n)
l=len(str(n))
l1=len(n1)
n1=n1[l1-l:]
if int(n1)==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")