def numbers(n1,n2=10):
    print("number 1=",n1)
    print("number 2=",n2)

(numbers(20,30))
(numbers(50))

def result(n1,n2):
    print("number 1=",n1)
    print("number 2=",n2)

result(50,30)
print("passing single argument")
try:
   result(10)
except:
   print( "Function needs two positional arguments" ) 

