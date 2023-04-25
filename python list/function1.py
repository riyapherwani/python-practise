def squares(item_list):
    squares1=[]
    for i in item_list:
        squares1.append(i**2)
    return squares1

my_list=[12,13,14,15]
res=squares(my_list)
print(res)