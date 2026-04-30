# decorator function (that will be use to add extra behavour to the existing function without modifying it)
# def decorator_func(main_fun):
#     def wrapper():
#         print("before calling the main function")
#         main_fun()
#         print("after calling the main function")
#     return wrapper

# @decorator_func
# def abc():
#     print("hello this is samarth")

# abc()

# real example

def login_check(main_fun):
    def wrapper(username, password):
        if username == "admin" and password == "password":
            print("Login successful")
            main_fun(username)
        else:
            print("Login failed")
    return wrapper

@login_check
def user(username):
    print(f"welcome {username}")
user("admin", "password")
