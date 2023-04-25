# Create a list of tuples that contain the index and value of each element in a given list using list comprehension.
# my_list = ["apple", "banana", "cherry"]
l1=[]
my_list = ["apple", "banana", "cherry"]

l1=[(i,my_list[i]) for i in range(0,len(my_list))]
new_tuple= tuple(l1)
print(new_tuple)

