name = "samarth"

# give the lenth of string 
print(len(name))

# check name with th or not using ends with or start with  
print(name.endswith("th"))
print(name.endswith("tssh"))
print(name.startswith("sam"))

# it use to first letter convert to capitalize
print(name.capitalize())

# new style to use variable in string format use a f string mark 
a = input("enter your name ")
print(f"Good moring {a}")

# use a replace a data in print using repalce keyword
x = ''' hello <|<name|> , 
you are selected in my group
<|date|>'''
print(x.replace("<|<name|>","samarth chavda").replace("<|date|>","30 may 2026"))