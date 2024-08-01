import random
i = random.randrange(1,101)
print("The random number is: ", i)
for j in range(1,101):
    if(j==i):
        break
    print(j)

