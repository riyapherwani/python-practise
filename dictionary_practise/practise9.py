str="k1,v1,k2,v2,k3,v3,k4,v4,k5,v5"
import json

string = '{"key1": "value1", "key2": "value2", "key3": "value3"}'
dictionary = json.loads(string)
print(dictionary)

string1 = "{'key1': value1, 'key2': value2, 'key3': value3}"
dictionary1 = eval(string)
print(dictionary1)