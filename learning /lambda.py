# lambda is a small anonymous function that can take any number of arguments, 
# but can only have one expression. The syntax for a lambda function is
# Syntax = lambda arguments: expression

add = lambda a,b : a + b
print(add(5, 3))

square = lambda x : x * x
print(square(12))

# with map()
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2,numbers))
print(result)

# with filter()
numbers = [1,2,3,4,5]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

# with sort()
student = [(100,"samarth"),(255,"chavda"),(38,"abc")]
sorted_list = sorted(student, key=lambda x: x[0])
print(sorted_list)