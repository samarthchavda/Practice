# 1. Write a program to find the greatest of four numbers entered by the user.

# type 1

'''numbers = []

for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

greatest = max(numbers)
print("The greatest number is:", greatest)'''

# type 2

'''a1 = int(input("Enter a Number 1 :"))
    a2 = int(input("Enter a Number 2 :"))
    a3 = int(input("Enter a Number 3 :"))
    a4 = int(input("Enter a Number 4 :"))

    if(a1>a2 and a1>a3 and a1>a4):
        print("Greatest Number is a1", a1)

    elif(a2>a1 and a2>a3 and a2>a4):
        print("Greatest Number is a2", a2)

    elif(a3>a1 and a3>a2 and a3>a4):
        print("Greatest Number is a3", a3)

    if(a4>a1 and a4>a3 and a4>a2):
        print("Greatest Number is a4", a4)'''

# '''2.Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.'''

'''marks = []
for i in range(3):
    num = int(input(f"enter a marks{i+1}: "))
    marks.append(num)
average = sum(marks) / 3

if average >= 40 and all(mark >= 33 for mark in marks):
    print("You are passed")
else:
    print("You are failed", average)
'''

#     '''3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams'''

'''p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

msg = input("Enter a Message ")

if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("this comment is spam")
else:
    print("this comment is not spam")
'''

#     '''4. Write a program to find whether a given username contains less than 10
# characters or not.'''

'''username = input("Enter a username ")

if(len(username)<10):
    print("very good name")
else:
    print("enter a valid username")'''

# '''5. Write a program which finds out whether a given name is present in a list or not'''

li = ["samarth","aman","harry","kirtan","yash"]
name = input("Enter your name : ").lower()# Lower is use to when user write a lower or upper case then show to check correct or not   
if(name in li):
    print("your name in the list")
else:
    print("your name is not in the list ")
