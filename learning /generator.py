# generator (it is a function that return value one by one )
# def numbers():
#     yield 100
#     yield 200
#     yield 300

# for num in numbers():
#     print(num)

# in loop
# def count_up(n):
#     for i in range(n):
#         yield i

# for num in count_up(15):
#     print(num)

# reading large file
# def read_file(file):
#     for line in file:
#         yield line
# with open("sample.txt", "r") as f:
#     for line in read_file(f):
#         print(line.strip())

nums =  (x*x for x in range(10))
for n in nums :
    print(n)