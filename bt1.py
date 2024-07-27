#bai1
# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position

#     def say_hi(self):
#         print(f"Hi, my name is {self.name}.")

#     def tell_position(self):
#         print(f"I am a {self.position}.")


# john = Employee("John", "Software Engineer")
# john.say_hi()
# john.tell_position()




#Bai2
# import math
# class hinhtron:
#     def __init__(self, bankinh):
#         self.bankinh = bankinh
    
#     def cv(self):
#         return 2 * math.pi * self.bankinh
    
#     def dt(self):
#         return math.pi * self.bankinh ** 2

# class hinhchunhat:
#     def __init__(self, cd, cr):
#         self.cd = cd
#         self.cr = cr

#     def chuvi(self):
#         return (self.cd + self.cr) * 2

#     def dientich(self):
#         return self.cd * self.cr
    
# a = input("nhap hinh muon tinh (hinh chu nhat | hinh tron): ")

# if a == "hinh tron":
#     b = int(input("nhap ban kinh hinh tron: "))
#     ht = hinhtron(b)
#     print("chu vi hinh tron la:", ht.cv())
#     print("dien tich hinh tron la:", ht.dt())
# elif a == "hinh chu nhat":
#     c = int(input("nhap chieu dai hcn: "))
#     d = int(input("nhap chieu rong hcn: "))
#     hcn = hinhchunhat(c, d)
#     print("chu vi hinh chu nhat la:", hcn.chuvi())
#     print("dien tich hinh chu nhat la:", hcn.dientich())
# else:
#     print("hinh khong hop le")





#bai3
# from datetime import datetime
# class CustomDate:
#     def __init__(self):
#         self.now = datetime.now()
    
#     def get_date(self):
#         return self.now.strftime("%d/%m/%Y")
    
#     def get_time(self):
#         return self.now.strftime("%H:%M:%S")

# now = CustomDate()
# print(now.get_date())
# print(now.get_time())





#bai4
from datetime import datetime
class DateHandler:
    def ngay(date):
        return date.strftime("%d/%m/%Y")
    
    def ngay_giua(date1, date2):
        return (date2 - date1).days

start_date = datetime(2021, 1, 1)
end_date = datetime(2023, 2, 3)

print("start:", DateHandler.ngay(start_date))
print("end:", DateHandler.ngay(end_date))
print("ngay giua:", DateHandler.ngay_giua(start_date, end_date))
        
        




