#merging two dictionary
d1={'name':'veer','age':'32'}
d2={'school':'DPS','number':'1233456'}
d1.update(d2)
print(d1)
swapped_dict={v:k for k,v in d1.items()}
print(swapped_dict)

#getting values of dictionary
print(d1.values())

#nested dictionary
d3={"rahul":{'id':'3205','sal':'23000'},"Amit":{'id':'2504','sal':'50000'}}
print(d3)
print(d3['rahul']['id'])
print(d3['Amit']['sal'])