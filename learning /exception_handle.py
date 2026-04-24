# # exception handle 
# try :
#     a = 10 / 0 
# except :
#      print("error")

# if else error check
# try :
#     a = 10 / 2
# except ZeroDivisionError:
#     print("error")
# else:
#     print("result is ",a)
# finally:
#     print("no error")



# example of real like 
# class LowBalanceError(Exception):
#     pass
# def withdraw(balance , amount):
#     if amount > balance:
#         raise LowBalanceError("Insufficient balance")
#     return balance - amount 
# try :
#     withdraw(10000, 2000)
# except LowBalanceError as e:
#         print(e)




# Api for backend user :
def login(user):
    if user is None:
        raise ValueError("User cannot be None")
    return "login successful"
try: 
    print(login(None))
except ValueError as e:
    print(e)
