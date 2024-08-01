# .................assignment operators...................
x = 3
y = 5
x+= 10
y-= 3
print(x+y)

# ..........logical operators..........
x = 3
y = 5
print(x<y and x!=y)
print(x>y or x!=y)
print(not(x>y and x<y))

# ............membership operators...........
x="hey! how are you? are you free at 5"
print('5' in x)

# ..........operator precedence............
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)#If two operators have the same precedence, the expression is evaluated from left to right.   