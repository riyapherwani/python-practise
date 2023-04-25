str="123455 "
res=str.isalnum()
print(res)

str = "1234567189 "
result=str.isalnum()
print("Are all the characters of the string alphanumeric?", result)

str = "Welcome////"
res=str.isalpha()
print(res)

a="12344"
b="yuhu23"
c="\n\n"
res1=a.isdigit()
res2=b.isdigit()
res3=c.isdigit()
res4=c.isspace()
res5=a.isspace()
print(res1," ",res2," ",res3," ")
print(res4," ",res5)