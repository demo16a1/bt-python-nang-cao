#nguyễn thị thuyên -22174600032
class Da_giac:
    def __init__(self,cao,day):
        self.cao = cao
        self.day= day
class Binh_hanh(Da_giac):
    def __init__(self,cao,day,ben):
        self.ben = ben
        Da_giac.__init__(self,cao,day)
    def chu_vi(self):
        print('chu vi',(self.day+self.ben)/2)
    def dien_tich(self):
        print('diện tích',self.day*self.cao)
class Chu_nhat(Binh_hanh):
    def __init__(self,cao,day,ben ):
        super().__init__(cao,day,ben)
        self.ben = self.cao
    def chu_vi(self):
        print('chu vi',(self.day+self.cao)*2)
    def dien_tich(self):
        print('diện tích',self.day*self.cao)
class Vuong(Chu_nhat):
    def __init__(self, cao, day, ben):
        super().__init__(cao, day, ben)
    def chu_vi(self):
        print('chu vi hình vuông',self.cao*4)
    def dien_tinh(self):
        print('diện tích hình vuông',self.cao *self.day)
hinh = ['Bình Hành','Chữ Nhật','Vuông']
for i in range(0,3):   
    print(f'mời nhập các thuộc tính cần thiết của hình {hinh[i]}:')
    if hinh[i] == 'Chữ Nhật' :
        cao = float(input('mời nhập chiều rộng hình chữ nhật'))
        day = float(input('mời nhập chiều dài hình chữ nhật'))
        ben = 0
        obj = Chu_nhat(cao,day,ben)
        obj.chu_vi()
        obj.dien_tich()
    elif hinh[i] == "Vuông":
        cao = float(input("mời nhập cạnh hình vuông"))
        ben = cao 
        day = cao
        obj2 = Vuong(cao,day,ben)
        obj2.chu_vi()
        obj2.dien_tich()
    else:
        cao = float(input('mời nhập chiều cao hình bình hành:'))
        day = float(input('mời nhập độ dài đáy hình bình hành:'))
        ben = float(input('mời nhập cạnh bên hình bình hành: '))
        obj3 = Binh_hanh(cao,day,ben)
        obj3.chu_vi()
        obj3.dien_tich()