# Write a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 10 and the values are the squares
#  of the corresponding keys.

dict={i:i**2 for i in range(1,11)}
print(dict)