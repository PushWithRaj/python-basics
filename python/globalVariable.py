#........Global variable...........!

x="snake"

def myfunc():
    x="awesome"
    print("Python is "+x)
myfunc()

print("Python is "+ x)

#........define global variable inside the fuction.......
def same():
    global y
    y = "Eassy"
    print("python is "+y)
same()

print("python is "+y)

#......change global variable through inside the fuction.......
z="good"
print("I am "+z)

def change():
    global z
    z="bad"
    print("I am "+z)
change()
print("I am "+z)