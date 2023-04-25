dict={'name':"zara",'age':"27"}
print(dict)
#accessing dict elements
print(dict['name'],dict['age'])

#updating dictionary 
dict['age']=32
print("Updated dictionary",dict)

#inserting elements in dictionary
dict['school']='DPS School'
print(dict)

#deleting dictionary 
del dict['name']
print(dict)
# dict.clear()
# del dict
# print(dict['age'])

#checks whether key exist in dictionary or not
# print(dict.has_key('age'))
print(dict.items())

#setdefault method
print(dict.setdefault('age',None))
print(dict.setdefault('Sex',None))