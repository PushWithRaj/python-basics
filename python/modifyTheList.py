# .........change and insert the elements...............

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# To change the value of a specific item, refer to the index number:
thislist[1] = "mango"
print(thislist)
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist,len(thislist))

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

thislist[1:2] = ["peach", "guava"]
print(thislist,len(thislist))

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

thislist[1:3] = ["fig"]
print(thislist,len(thislist))

# The insert() method inserts an item at the specified index:
thislist.insert(2, "pomegranate")
print(thislist,len(thislist))

# insert multiple elements.........
thislist.insert(2, ["litchi","papaya"])
print(thislist,len(thislist))

#add list items through many methods...........
    #   1.append() method......
thislist.append("orange")       
print(thislist)
    # 2. extend() methog.........
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)                           
print(thislist)
    #Add Any Iterable
evergreen = ("banana", "orange")
tropical.extend(evergreen)
print(tropical)

# for remove the list items..........
# 1.remove() method...........
tropical.remove("pineapple")
print(tropical)

#if there are more than one element is same then remove() function removes only first one...exp
thislist.remove("orange")
print(thislist)

# 2.pop() method...........
tropical.pop(2)
print(tropical)
#if we don't know the specify index then the pop() funtion removes the last element of the list....
thislist.pop()
print(thislist)

# 3.The del keyword also removes the specified index...............
del thislist[0]
print(thislist)

# Clear the List
# The clear() method empties the list. The list still remains, but it has no content.
thislist2 = ["apple", "banana", "cherry"]
print(thislist2)
thislist2.clear()
print(thislist2)
# The del keyword can also delete the list completely.  Delete the entire list..........
thislist2 = ["apple", "banana", "cherry"]
del thislist2
 