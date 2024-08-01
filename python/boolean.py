#........... some boolean outcomes statemants............
print(10 > 9)
print(10 == 9)
print(10 < 9)
print("  ")
print("  ")

#............some false boolean values ....................
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(False))

#............ false fucntion...............
print("in class")
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#.......... isinstance function..........
x = 200
print(isinstance(x, int))
