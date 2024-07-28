# class nhanvat:
#     def __init__(self, toc, tuoi):
#         self.toc = toc
#         self.tuoi = tuoi
    
#     def dam(self):
#         return "-50 mau"
    
#     def da(self):
#         return "-70 mau"
    
#     def info(self):
#         print([self.toc, self.tuoi])


# Huy = nhanvat("đen", 25)
# Huy.info()
# print(Huy.dam())
# print(Huy.da())



# class nhanvat:
#     def __init__(self, toc, tuoi):
#         self.toc = toc
#         self.tuoi = tuoi
    
#     def dam(self):
#         return "-50 mau"
    
#     def da(self):
#         return "-70 mau"
    
#     def info(self):
#         print([self.toc, self.tuoi])

# class chienbinh(nhanvat):
#     def __init__(self, toc, tuoi, vu_khi):
#         super().__init__(toc, tuoi)
#         self.vu_khi = vu_khi
    
#     def info(self):
#         super().info()
#         print("Vu khi:", self.vu_khi)

#     def danh_kem_vu_khi(self):
#         return "-100 mau"

# Huy = nhanvat("đen", 25)
# Quang = chienbinh("nâu", 30, "kiem")
# Huy.info()
# print(Huy.dam())
# print(Huy.da())
# Quang.info()
# print(Quang.dam())
# print(Quang.da())
# print(Quang.danh_kem_vu_khi())


class nhanvien:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
    
    def info(self):
        return f"Tên: {self.ten}, Tuổi: {self.tuoi}"

class nhanvienchinhthuc(nhanvien):
    def __init__(self, ten, tuoi, luongcb, hesoluong):
        super().__init__(ten, tuoi)
        self.luongcb = luongcb
        self.hesoluong = hesoluong
    
    def tinhluong(self):
        return self.hesoluong * self.luongcb
    
    def info(self):
        base_info = super().info()
        return f"{base_info}, Lương cơ bản: {self.luongcb}, Hệ số lương: {self.hesoluong}, Lương: {self.tinhluong()}"

class nhanvienthoivu(nhanvien):
    def __init__(self, ten, tuoi, sogio, luongtheogio):
        super().__init__(ten, tuoi)
        self.sogio = sogio
        self.luongtheogio = luongtheogio
    
    def tinhluong(self):
        return self.sogio * self.luongtheogio
    
    def info(self):
        base_info = super().info()
        return f"{base_info}, Số giờ làm việc: {self.sogio}, Lương theo giờ: {self.luongtheogio}, Lương: {self.tinhluong()}"

class Department:
    def __init__(self, ten_phong):
        self.ten_phong = ten_phong
        self.danh_sach_nhan_vien = []
    
    def them(self, nhan_vien):
        self.danh_sach_nhan_vien.append(nhan_vien)
        print(f"Đã thêm nhân viên: {nhan_vien.ten}")
    
    def xoa(self, nhan_vien):
        if nhan_vien in self.danh_sach_nhan_vien:
            self.danh_sach_nhan_vien.remove(nhan_vien)
            print("Xa thai:",nhan_vien.ten)
        else:
            print("nhan vien khong ton tai")

    def nhanvienxathai(self):
        for nhan_vien in self.danh_sach_nhan_vien:
            print("nhan vien con lai:" + nhan_vien.ten )
    def info(self):
        print("phong ky thuat:")



Huy = nhanvienchinhthuc("Huy", 25, 6000000, 10)
Tai = nhanvienthoivu("Tai", 20, 160, 20000)

phong_ky_thuat = Department("Kỹ Thuật")
phong_ky_thuat.them(Huy)
phong_ky_thuat.them(Tai)

phong_ky_thuat.info()

print(Huy.info())
print(Tai.info())

phong_ky_thuat.xoa(Tai)
phong_ky_thuat.nhanvienxathai()






    


