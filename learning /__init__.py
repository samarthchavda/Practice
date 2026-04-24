# class person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f"my name is {self.name} and my age is {self.age}")

# p1 = person("samarth", 21)
# p1.display()

# class dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         print(self.name)
# d1 = dog("buddy",3)
# d1.bark()


# class Car:
#     def __init__(self,brand):
#         self.brand = brand
#     def show(self):
#         print("this is the car brand " + self.brand)

# c1 = Car("Ford")
# c1.show()


# class Student:
#     def __init__(self,name, grade):
#         self.name = name
#         self.grade = grade
# s1 = Student("Anna", "A")
# print(s1.grade)
# s1 = Student("Anna", "B")
# print(s1.grade)


# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
# r1 = Rectangle(5, 3)
# print(r1.area())


# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         print(self.name)
# class Dog(Animal):
#     pass
# d1 = Dog("rex")
# d1.speak()

# polymorphism (same function different behavior)
# class Cat:
#     def Sound(self):
#         print("meow")
# class Fox: 
#     def Sound(self):
#         print("Wa-pa-pa-pa-pa-pow!")
# c1 = Cat()
# f1 = Fox()
# for animal in (c1,f1):
#     animal.Sound()

# class ScoreBoard:
#     def __init__(self,score):
#         self.score = score  
#     def get_score(self):
#         return self.score
# s1 = ScoreBoard(0)
# print(s1.get_score())

# encapsulation (hiding the data)
# it is proctecing inside a claas using like private property __prefix
class ScoreBoard:
    def __init__(self,score):
        self.__score = score  
    def get_score(self):
        return self.__score
s1 = ScoreBoard(0)
print(s1.get_score())
