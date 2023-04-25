# Write a dictionary comprehension to create a dictionary where the keys are the names of states and the values are their abbreviations.
list={'Madhya Pradesh','Andhra Pradesh','Tamil Nadu','Himachal Pradesh'}
new_str=" ".join(list)
print(new_str)
new_list=new_str.split(" ")
print(new_list)
dict={i:i[0] for i in new_list }
print(dict)