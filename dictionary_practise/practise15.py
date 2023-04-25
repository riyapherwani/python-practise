# Write a dictionary comprehension to create a dictionary where the keys are the names of animals and the values are their average weights.
animals_weight=[('Tiger',108),('lion',115),('rabbit',65),('panther',158)]
dict={animals:weight/len(animals_weight) for animals,weight in animals_weight}
print(dict)