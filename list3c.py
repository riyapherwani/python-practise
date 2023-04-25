# Create a list of prime numbers from 1 to 50 using list comprehension.

n=int(input("Enter the number till you want prime numbers"))
print(type(n))
l3=[x for x in range(2, int(n))
     if all(x % y for y in range(2, int(x/2)+1))]
print(l3)

