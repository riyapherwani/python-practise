# generate square of first 10 odd numbers using list comprehension
# l1=[i**2 for i in range(1,21) if i%2!=0]
# print(l1)

count=1
i=2
while(count<=10):
  b=0
  for j in range(2,int(i/2)+1):
      if(i%j==0):
        b=1
        break
  if(b==0):
    print(i,end=',')
    count=count+1
  i=i+1
  
      