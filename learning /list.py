
list = ["samarth","chavda",6,10,"apple","banana"]   
list1 = ["abc","def","grapes","orange"]
# print(list)
# print(len(list))
# print(list[-3]) #negative index value start from last data and show the data
# print(list[:4]) #skipping last two data and show the rest of data
# print(list[2:]) #skipping first two data and show the rest of data
# print(list[-4:-1]) #range of list

# list[2] = "shubham" #change the data in list using index value 
# print(list) 

# list.append("marwadi university") #add the data in list using append
# print(list)

# list.insert(2, "raju") #insert data at index 2
# print(list)

# list.extend(list1) #add the list1 data in list using extend
# print(list)

# list.remove("raju") #remove the data in list
# print(list)

# list.pop(5) #remove the last data in list
# print(list) 

# # del list[0] #delete the data in list using index value
# # print(list)

# # list.clear() #clear the list
# # print(list)




# # loops wise 

# for x in list1:
#     print(x)    
#     # print(len(x))

# for loop print all item in list 
# [print(x) for x in list1]

# i = 0 
# while i < len(list1):
#     print(list1[i])
#     i = i + 1

fruit = ["apple","banana","grapes","orange","kiwi","melon"]
newlist = [5,6,12]    
# for x in fruit:
#     if "a" in x:
#         print(x)
#         newlist.append(x)
# print(newlist)



# two list add using for loop
# for x in newlist:
#     fruit.append(x)
# print(fruit)

# newlist = [x.upper() for x in fruit]
# newlist = ['hello' for x in fruit]
# fruit.sort()
# fruit.reverse()

# copy list 
# mylist = fruit.copy()   
# mylist = newlist+ fruit
# print(mylist)

# extend use to add two list 
fruit.extend(newlist)
print(fruit)

# print(fruit)
# print(newlist)
