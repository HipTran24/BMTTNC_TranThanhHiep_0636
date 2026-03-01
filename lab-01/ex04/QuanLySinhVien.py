from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        maxId = 1
        if self.soLuongSinhVien() > 0:
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if maxId < sv._id:
                    maxId = sv._id
            maxId += 1
        return maxId

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))

        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            sv._name = input("Nhap ten sinh vien: ")
            sv._sex = input("Nhap gioi tinh sinh vien: ")
            sv._major = input("Nhap chuyen nganh cua sinh vien: ")
            sv._diemTB = float(input("Nhap diem cua sinh vien: "))
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co ID = {} khong ton tai".format(ID))

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB)

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None

    def findByName(self, keyword):
        result = []
        for sv in self.listSinhVien:
            if keyword.upper() in sv._name.upper():
                result.append(sv)
        return result

    def deleteById(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.listSinhVien.remove(sv)
            return True
        return False

    def xepLoaiHocLuc(self, sv):
        if sv._diemTB >= 8:
            sv._hocLuc = "Gioi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Kha"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<12} {:<8} {:<12}".format(
            "ID", "Name", "Sex", "Major", "DiemTB", "Hoc Luc"
        ))
        for sv in listSV:
            print("{:<8} {:<18} {:<8} {:<12} {:<8} {:<12}".format(
                sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc
            ))
        print()

    def getListSinhVien(self):
        return self.listSinhVien