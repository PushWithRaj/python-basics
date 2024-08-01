#created a list..........

list1 = [1,2,3,4,5,6,7,8]
print(list1)
thislist = ["apple","banana","cherry"]
print(thislist)
# find the length/no.of elements of list..........
print(len(list1),len(thislist))

# check data type..........
list2 = ["abc", 34, True, 40, "male"]
print(type(list1))

#list keyword.....
list3 = list(("apple","banana","cherry"))
print(list3)

# access list item through indexing..........
print(list1[1],thislist[1])
# access list item through negative indexing..........
print(list1[-4],thislist[-1])
#....access specify elements of lists through "range of indexing"..........
print(list1[1:4],thislist[1:3])

print(list1[:4],thislist[1:])
print(list1[-4:-1])
# Check if Item Exists, To determine if a specified item is present in a list use the in keyword:
print("apple" in thislist)