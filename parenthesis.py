str=['[','(','[',']',')','}']
flag=0
new_list=[]
for i in range (0,len(str)):
    if(len(str)%2==0):
        flag=0
        break
    elif (str[i]=='[' or str[i]=='(' or str[i]=='{'):
        new_list.append(str[i])
        if(str[i]=='['):
            if(new_list[-1]==']'):
                new_list.pop()
        elif(str[i]=='('):
            if(new_list[-1]==')'):
                new_list.pop()
        elif(str[i]=='{'):
            if(new_list[-1]=='}'):
                new_list.pop()

        

if(new_list):
    print("Invalid String")
else:
    print("Valid String")    