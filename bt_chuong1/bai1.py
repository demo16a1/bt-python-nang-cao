#Nguyễn Thị Thuyên-22174600032
class hinhchunhat:
    def __init__(self):
        self.chieudai=float(input('chiều dài: '))
        self.chieurong=float(input('chiều rộng: '))
    def tinhchuvi(self):
        chuvi=(self.chieudai+self.chieurong)*2
        print('chu vi của hình chữ nhật :',chuvi)
    def tinhdientich(self):
        dientich=self.chieudai*self.chieurong
        print('diện tích của hình chữ nhật :',dientich)
canh=hinhchunhat()
canh.tinhchuvi()
canh.tinhdientich()

