class NhanVien:
    def __init__(self, tenNhanVien, luongCoBan, heSoLuong, luong_max):
        self.tenNhanVien = tenNhanVien
        self.luongCoBan = luongCoBan
        self.heSoLuong = heSoLuong
        self.luong_max = luong_max

    def in_tt(self):
        print(self.tenNhanVien, self.luongCoBan, self.heSoLuong, self.luong_max)

    def tinh_Luong(self):
        luong = self.heSoLuong * self.luongCoBan
        return luong


class TruongPhong(NhanVien):
    def __init__(self, tenNhanVien, luongCoBan, heSoLuong, luong_max, phuCap, soNamDuongChuc):
        super().__init__(tenNhanVien, luongCoBan, heSoLuong, luong_max)
        self.phuCap = phuCap
        self.soNamDUongChuc = soNamDuongChuc

    def in_tt(self):
        print(self.tenNhanVien, self.luongCoBan, self.heSoLuong, self.luong_max, self.phuCap, self.soNamDUongChuc,)

    def tinh_Luong(self):
        luong = self.heSoLuong * self.luongCoBan + self.phuCap
        return luong


emp1 = NhanVien("Tran Dan", 4000000, 1.20, 100000000)
emp2 = NhanVien("Nguyen Van Thieu", 4000000, 1.10, 100000000)
emp3 = TruongPhong("Lisa", 10000000, 1.40, 200000000, 200, 5)
emp4 = emp1
emp1.in_tt()
print(f"luong cua nhan vien 1: {emp1.tinh_Luong()}")
emp2.in_tt()
print(f"luong cua nhan vien 2: {emp2.tinh_Luong()}")
emp3.in_tt()
print(f"luong cua nhan vien 3: {emp3.tinh_Luong()}")
emp4.in_tt()



