# ..........string indexing............

x = "hello, world"
print(x[1])
# ....... strint length.......
print("    ",len(x))
# ..........string looping..
for i in range(len(x)):
    print(x[i])

print("hello" in x)

# .............string slicing...........
print("          slicing           ")

print("normal slicing: ",x[2:5])
print("negative slicing: ",x[-5:-2])
print("slice from start : ",x[:5])
print("slice to the end: ",x[2:])