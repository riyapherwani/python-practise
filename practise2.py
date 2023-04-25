#  Reverse words in a given String in Python
s1="The black fox jumps over the lazy dog"
# print(s1.reverse())
# print(dir(s1))
# for i in s1:
l1=s1.split(" ")
l1.reverse()
new_string=" ".join(l1)
print(new_string)