n=1
i=2
while ( n <= 10): # change this value for more numbers
    b=0
    for j in range(2,int(i/2)+1):
        if(i%j==0):
            b=1
            break  
    if(b==0):
        print(i,end=', ')
        n=n+1
    i=i+1