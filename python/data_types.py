#............data types..........

x=str("hello world"); y=type(x)
print(x," ",y)
x=int(20); y=type(x)
print(x," ",y)

x=float(20.5); y=type(x)
print(x," ",y)

x= complex(1j); y=type(x)
print(x," ",y)

x=["apple","banana"] ; z=list(("apple","banana")); y=type(x)
print(x," ",z,"  ",y)

x= range(6); y=type(x)
print(x," ",y)

x={"name":"john","age":36} ; z=dict(name="john",age=36); y=type(x)
print(x," ",z,"  ",y)

x={"appe","banana"} ; z= set(("apple","banana")); y=type(x)
print(x," ",z,"  ",y)

x= frozenset({"apple","banana"}); y=type(x)
print(x," ",y)

x= True ; z= bool(5); y=type(x)
print(x," ",z,"  ",y)

x=b"hello" ; z=bytes(5); y=type(x)
print(x," ",z,"  ",y)

x= bytearray(5); y=type(x)
print(x," ",y)

x=memoryview(bytes(5)); y=type(x)
print(x," ",y)

x= None; y=type(x)
print(x," ",y)

b=23j
print(type(b))