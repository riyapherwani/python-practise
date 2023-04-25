# Write a dictionary comprehension to create a dictionary where the keys are the names of vegetables and the values are their prices per pound.
veg_name=[('tomato',15),('carrot',50),('cabbage',30)]
veg_per_pound={veg:price*2.204 for veg,price in veg_name}
print(veg_per_pound)

# Write a dictionary comprehension to create a dictionary where the keys are the names of books and the values are their authors.
# books_name=['Geeta','7 secrets of life','Revolution 2020']
# authors=['Vedvyas','Thomas Slyvia','Chetan bhagat']
# dict_book={book:author for book,author in zip(books_name,authors)}
# print(dict_book)

books_name=[('Geeta','Vedvyas'),('7 secrets of life','Thomas Slyvia'),('Revolution 2020','Chetan bhagat')]
dict_book={book:author for book,author in books_name}
print(dict_book)

