# Write a dictionary comprehension to create a dictionary where the keys are the first 10 numbers of the Fibonacci sequence and 
# the values are their corresponding indices.
fab_list=[]
f1=-1
f2=1
for i in range(1,11):
    sum=f1+f2
    fab_list.append(sum)
    f1=f2
    f2=sum
print(fab_list)
dict={i :fab_list[i] for i in range(0,len(fab_list))}
print(dict)