#bai1
# class Rectangle:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width

#     def __str__(self):
#         return f"Rectangle object with height = {self.height} and width = {self.width}"


# rect = Rectangle(2, 1)
# print(rect)



#bai2
# class MathList:
#     def __init__(self, values):
#         self.values = values
    
#     def __str__(self):
#         return str(self.values)
    
#     def __add__(self, number):
#         return [x + number for x in self.values]
    
#     def __sub__(self, number):
#         return [x - number for x in self.values]

# mathlist= MathList([1, 2, 3, 4, 5])
# print(mathlist)
# mathlist += 2
# print(mathlist)



#bai3
# class hinhvuong:
#     def __init__(self,dodai):
#         self.dodai = dodai
    
#     def dt(self):
#         return self.dodai*self.dodai
    
# class lp(hinhvuong):
#     def dt(self):
#         return self.dodai*self.dodai*6
#     def tt(self):
#         return self.dodai*self.dodai*self.dodai

# hv=hinhvuong(4)
# print("dt hinh vuong la:",hv.dt())
# lapphuong=lp(4)
# print("dt hlp la:",lapphuong.dt())
# print("tt hlp la:",lapphuong.tt())



#bai4
from datetime import datetime
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def welcome(self):
        print(f"Welcome, {self.username}")

    def check_password(self, password):
        return self.password == password

class SubscribedUser(User):
    def __init__(self, username, password, expiry_date):
        super().__init__(username, password)
        self.expiry_date = expiry_date

    def is_expired(self):
        return datetime.now() > self.expiry_date

user = User('mindx', '12345')
user.welcome()
print(user.check_password('1234'))

s_user = SubscribedUser('s_mindx', '1234', datetime(2021, 1, 1))
s_user.welcome()
print(s_user.check_password('1234'))
print(s_user.is_expired())
