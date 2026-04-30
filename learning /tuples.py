# tuples is store a multiple value in one varible and it is immutable in python
# that is unchangeable
# you cannnot remove in tuples

a = (1,2,5,5,100,"chavda","marwadi","raju")

# print(type(a))
# print(a[5])
# print(a[-1])
# print(a[1:5])
# print(a[1:])
# print(a[:5])

# # item exist or not 
# if "chavda" in a:
#     print("yes")
# else:   print("no")

# # convert the tuple into list
# X = list(a)
# X[2] = "rahul"
# Y= tuple(X)
# print(Y)

# # they dont have use to append but tuple convert into list and use append 
# x = list(a)
# x.append("ABC")
# y = tuple(x)    
# print(y)

# # add tuple to a tuple 
# new_tuple = (1, 2, 3)
# a += new_tuple
# print(a)

# # remove the data in tuple using list and convert into tuple again
# x = list(a)
# x.remove("marwadi")
# y = tuple(x)
# print(y)

# # delete tuple
# del a 
# print(a) #there is show error because we delete the tuple

# # If the number of variables is less than the number of values, 
# # you can add an * to the variable name and the values will be assigned to the variable as a list:
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# (green, *yellow, red) = fruits

# print(green) 
# print(yellow)  
# print(red)     



# # loops in tuples
# for x in a:
#     print(x)

# for x in range(len(a)):
#     print(a[x])

# # while loop
# i = 0 
# while i < len(a):
#     print(a[i])
#     i = i + 1   

# # join two tuples
# t1 = (1, 2, 3)
# t2 = ("samarth","cat","marwadi")
# t3 = t1 + t2
# print(t3)

# # multiply in tuple
# new = a * 4
# print(new)