thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# for x in thisdict:print(thisdict[x])
d_swap = {v: k for k, v in thisdict.items()}
print(d_swap)

swapped_dict={v:k for k,v in thisdict.items()}