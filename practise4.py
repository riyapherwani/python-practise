# generate square of first 10 natural numbers / do the same using list comprehension
for i in range(1,11):
    res=i**2
    print(res)

#Using list comprehension
li=[x**2 for x in range(1,11)]
print(li)