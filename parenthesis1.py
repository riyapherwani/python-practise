str='[]()'
new_str=[]
flag=0
for i in range (0,len(str)):
    if(str[i]=='[' or str[i]=='(' or str[i]=='{' ):
        new_str.append(str[i])
    elif(str[i]==']' or str[i]==')' or str[i]=='}'):
        if(new_str[len(new_str)-1])
if(len(new_str)==0):
    print("Valid String")     
else:
    print("Invalid String")    