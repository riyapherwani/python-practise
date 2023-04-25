import random
print("randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2))

print ("choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
print ("choice('A String') : ", random.choice('A String'))

print("Any random number is ",random.random())

random.seed(10)
print("Any random number is ",random.random())

list=[10,20,30,40,50]
random.shuffle(list)
print("New reshuffled list :",list)

print("random numbers between 5-10 is :",random.uniform(5,10))
