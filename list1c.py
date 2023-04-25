# Create a list of words that start with the letter "s" from a given list of strings using list comprehension.
# words = ["apple", "banana", "cherry", "strawberry", "orange", "kiwi"]

words=["apple", "banana", "cherry", "strawberry", "orange", "kiwi"]
new_list=[x.capitalize() for x in words if (x[0].upper()=='S' and x[-1].lower()=='y')]
print(new_list)
