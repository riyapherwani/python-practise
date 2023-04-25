#accessing the values of list
l1=[1,2,3,4,5,6,7]
print(l1[2],l1[5])
print(l1[2:5])

#updating the values of the list
print("ORiginal value",l1[2])
l1[2]=5
print("Updated value is :",l1[2])

#deleting the elements from the list
print("ORiginal list",l1)
print("Original length",len(l1))
del l1[2]
print("after deletion list is :",l1)
print("Length after deletion :",len(l1))