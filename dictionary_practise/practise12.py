# Write a dictionary comprehension to create a dictionary where the keys are the names of fruits and the values are their lengths.
list=['apple','banana','strawberry','cherry']
dict={i:len(i) for i in list}
print(dict)