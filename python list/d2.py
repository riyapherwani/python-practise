dict1={'[1,2,3]':'(1,4,9)','[4,5,6]':'[16,25,36]'}
print(dict1)

print(len(dict1))
dict1['ram']="setu"
print(len(dict1))

print(str(dict1))
print(type(dict1))

#copying dictionary 
dict2=dict1.copy()
print("Dictionary 2 is:",dict2)

#creating dictionary from the list
list1=('name','address','number')
dict2=dict2.fromkeys(list1,10)
print(dict2)

# fetching values from keys
print(dict1.get('[1,2,3]'))
print(dict1.get("Education","Never"))

print(dict1.keys())

