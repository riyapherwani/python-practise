# Write a function that takes two dictionaries as input and returns a new dictionary that represents the difference of the two dictionaries.
#  The difference should only include key-value pairs that are present in the first dictionary but not in the second.

def differ(dict1,dict2):
    new_dict=dict()
    new_dict.update(dict1.items)
    return new_dict

dict1={"brand": "Ford","model": "Mustang","year": 1964}
dict2={"brand": "Mercedes",
  "model": "Mustang",
  "year": 1956}
res=differ(dict1,dict2)
print(res)

