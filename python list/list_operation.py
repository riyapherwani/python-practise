list1=[2,6,20,80]
list2=[2,3,6,7]
# print(cmp(list1,list2))
print(max(list2))
print(min(list2))

#converting tuple into list
tup=(1,2,3,4,5)
print("This is our tuple ",tup)
alist=list(tup)
print("This is our list",alist)

#cerating empty list

l1= {2:3}
# l1=list(input())
# l1.append(i)
print("Our final list is :",l1)
print(type(l1))

for i in list1:
    print(i)