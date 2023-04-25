res=lambda a,b:a+b;
print(res(30,40))
print(res(90,120))

# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function
#  that multiplies argument x with argument y and prints the result.

plus=lambda x:x+15;
multiply=lambda x,y:x*y;
print(multiply(20,10))
print(plus(30))

l1=[3,7,1,2,10,4]
sorted(l1)
print(l1)
l1.sort(key=lambda x: 100/x)
print(l1)

# Using sorted() function and lambda sort the words in the list based on their second letter from a to z.
lst=["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]

lst=sorted(lst,key=lambda x:x[1])
print(lst)

mylist = [3, 6, 3, 2, 4, 8, 23]
sorted(mylist, key=lambda x: x % 2 == 0)
print(mylist)

mylist1 = [(3, 5, 8), (6, 2, 8), (2, 9, 4), (6, 8, 5)]
sorted(mylist1, key=lambda x: x[1])
print(mylist1)
