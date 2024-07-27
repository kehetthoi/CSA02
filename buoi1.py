a = int(input("Nhập chiều dài: "))
b = int(input("Nhập chiều rộng: "))

class Chunhat:
    def __init__(self, canh, goc):
        self.canh = canh
        self.goc = goc

    def chuvi(self):
        return (self.canh + self.goc) * 2

    def dientich(self):
        return self.canh * self.goc

hinhchunhat = Chunhat(a, b)

print("Chu vi hình chữ nhật:", hinhchunhat.chuvi())
print("Diện tích hình chữ nhật:", hinhchunhat.dientich())
