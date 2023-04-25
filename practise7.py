# - extract unique values from dictionary

dict=[{'name1':'rohan','name2':'rohan','name3':'riya','name4':'pherwani'}]
print("ORIGINAL LIST :"+str(dict))
res = list(set(val for dic in dict for val in dic.values()))
print("UNIQUE LIST"+str(res))
y=str(res)
print(type(str))