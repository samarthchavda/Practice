# # sets are store multiple items in one variable
# # it is writing in curly brackets and it is unordered and unindexed

a = {1,2,"raju","rohit","samarth","chavda",True}
# # print(a)
# # print(type(a))
# # print(len(a))

# for x in a:
#     print(x)
 
# print("raju" not in a)
# print("Ramu" in a) # check the item exist or not

# # add() method is used to add the item in set
# a.add("ABC")
# print(a)

# # add two set using update() method
# x = {"apple", "banana", "cherry"}
# y = {"pineapple", "mango", "papaya"}
# x.update(y)
# print(x)

# # remove() method is used to remove the item in set
# a.remove("rohit")   
# print(a)
# a.discard("samarth") 
# print(a)
# a.pop()
# print(a)
# a.clear()
# print(a)
# del a 
# print(a) #showing error because we delete the set


# # join sets 
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# s3 = set1.union(set2)
# print(s3)

# s3 = set1 | set2
# print(s3)   

# # join multiple sets
# set = set1.union(set2,set3,set4)
# set = set1 | set2 | set3 | set4    
# print(set)


# # join set and tuple
# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y)
# print(z)

# # update 
# x.update(y) 
# print(x)    



# In intersection() method will return a new set, that only contains the items that are present in both sets.
s1 = {"apple", "banana", "cherry"}
s2 = {"google", "microsoft", "apple"}
# s3 = s1.intersection(s2)
# print(s3)
# s3 = s1 & s2
# print(s3)   

# #  intersection_update() method will also keep ONLY the duplicates, 
# # but it will change the original set instead of returning a new set.

# s1.intersection_update(s2) 
# print(s1) 

# # difference() method will return a new set, 
# # that contains items that are only present in the first set, and not present in the second set.
# s3 = s1.difference(s2)
# s3 = s1 - s2    
# print(s3)

# # difference_update() method will remove the items that are present in both sets,
# # and keep only the items that are present in the first set.
# s1.difference_update(s2)
# print(s1)

# # symmetric_difference() method will return a new set,
# #  that contains only the items that are NOT present in both sets,
# s3 = s1.symmetric_difference(s2)
# print(s3)
# s3 = s1 ^ s2
# print(s3)   