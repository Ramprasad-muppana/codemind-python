for _ in range(int(input())):
    a,b=map(int,input().split())
   
    if a>=b:
        print(-1)
    else:
        for k in range(0,b):
            c=k*k
            c=c%b
            if c==a:
                print(k)
                break
            k=k+1
        else:
            print(-1)