# enter a 5 fruit name using for loop and give the array 
# items = []
# for i in range(5):
#     item = input(f"Enter a fruit name{i+1}: ")
#     items.append(item)
# print(items)

# input a marks and show in sorted from
mark = []
for i in range(6):
    a = int(input(f"Enter you subject mrks{i+1}:"))
    mark.append(a)
    mark.sort()
# Calculating the average
average = sum(mark) / len(mark)

print(mark)
print(f"avarage{average}")