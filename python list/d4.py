# Write a dictionary comprehension to create a dictionary where the keys are the first 10 letters of the alphabet and the values are
#  the corresponding ASCII codes.

dict1 ={chr(i):i for i in range(97,107)}
print(dict1)
