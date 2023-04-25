sum=0
f1=-1
f2=1
# n=int(input("Enter the number till you want fibonnaci series"))
# for i in range(0,n):
#     sum=f1+f2
#     f1=f2
#     f2=sum
#     print(sum)

n = 10 # number of terms to generate
fibonacci = [0, 1] +[fibonacci[i-1] + fibonacci[i-2] for i in range(2,10)]

print(fibonacci)