# Tuples are immutable in Python, which means you can’t add, remove, or modify elements after creation. 
# This is why tuples have fewer methods compared to lists.
a = [1,2,5,5,100,"chavda","marwadi"]

# 1. count method in  tupples 
no = a.count(5)
print(no)

#  2. Slicing Tuples
# You can extract parts of a tuple using slicing.
my_tuple = (0, 1, 2, 3, 4, 5)
print(my_tuple[1:4])  
print(my_tuple[:3])   
print(my_tuple[3:])    

# 3. Concatenation and Repetition
# Combining two tuples.
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2) 

# Repeating elements
t = (0, 1)
print(t * 3) 

# 4. Tuple with Functions
# Returning multiple values from a function
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print(x, y)  # Output: 10 20

# how tu sum in python 
list = [25,85,885,11]
print(sum(list))