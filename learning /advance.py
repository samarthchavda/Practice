# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# s1 = student("samarth",21)



# constructor(run automatically when object is created)
# def __init__(self, name):
#     self.name = name


# encapsulation(data hiding)
# class student:
#     def __init__(self, ):
#         self._name = samarth

#     def display(self):
#         return self._name


# inheritance
class Animal:
    def sound(self):
        print("animal speaks")
    
class cat(Animal):
    def bark(self):
        print("meow")

c = cat()
c.sound()
c.bark()


#polymorphism (same function different behavior)
# class animal:
#     def speak(self):
#         print("animal speaks")

# class dog:
#     def sound(self):
#         print("bark")

# class cat:
#     def sound(self):
#         print("meow")

# for animal in [dog(),cat()]:
#     animal.sound()



# abstract (hiding the complext logic, show only necessary part)
# from abc import ABC, abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class square(shape):
#     def area(self):
#         return 4*4


# magic methonds
# 1.__str__
# class abc:
#     def __init__(self,name):
#         self.name = name
    
#     def __str__(self):
#         return f"my name is {self.name}"

# a = abc("samarth")
# print(a)

# 2.__init__

# class abc: 
#     def __init__(self,name):
#         self.name = name

# a = abc("samarth")
# print(a.name)

# 3.__len__

# class abc:
#     def __init__(self,name):
#         self.name = name
    
#     def __len__(self):
#         return len(self.name)
# a = abc("samarth")
# print(len(a))

# 4.__add__(operator overloading)
# class abc:
#     def __init__(self,name):
#         self.name = name
    
#     def __add__(self, other):
#         return self.name + other.name
    
# a1 = abc("samarth ")
# a2 = abc("chavda")
# print(a1 + a2)

# 5.__eq__(comparsion operator )
# class abc:
#     def __init__(self,value):
#         self.value = value

#     def __eq__(self, other):
#         return self.value == other.value
# a1 = abc(10)
# a2 = abc(10)
# print(a1 == a2)

# 6.__getitem__(accessing list)
class abc:
    def __init__(self,data):
        self.data = data

    def __getitem__(self, index):
       return self.data[index]

a = abc([100,200,300,400,500])
print(a[2])