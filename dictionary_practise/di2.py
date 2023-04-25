#squaring numbers using dictionary comprehension
dict1={num: num*num for num in range(1,11)}
print(dict1)

old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)
