# Write a dictionary comprehension to create a dictionary where the keys are the even numbers from 1 to 10 and the values are their squares.
dict={i:i**2 for i in range(1,11) if i%2==0}
print(dict)