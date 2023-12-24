#Nguyễn Thị Thuyên-22174600032
class TS:
    def __init__(self,name,math,physic,chemistry):
        self.name = name
        self.math = math
        self.physic = physic
        self.chemistry = chemistry
        TS.ds=[]
    def thongtin(self,ketqua):
            self.name = input('Tên sinh viên: ')
            self.math = float(input("Điểm Toán: "))
            self.physic = float(input("Điểm Vật Lý: "))
            self.chemistry = float(input("Điểm Hóa: "))
            ketqua =[self.name,self.math,self.physic,self.chemistry]
            self.ketqua = ketqua
                    
    def total(self):
        tong = self.math + self.physic + self.chemistry
        self.ketqua.append(tong)
        TS.ds.append({'ho_ten':self.ketqua[0],'toan':self.ketqua[1],'ly':self.ketqua[2],'hoa':self.ketqua[3],\
                        'tong':self.ketqua[4]})
        
    @staticmethod
    def out():
        sorted_ds=sorted(TS.ds,key=lambda x: x['tong'],reverse=True)
        
        print("Danh sách thí sinh trúng tuyển")
        print('{:<15}{:^5}{:^5}{:^5}{:^20}'.format('Họ và tên','Toán','Lý','Hóa','Tổng điểm'))       
        for i in sorted_ds:
           if i['tong']>=20:
                print('{:<15}{:^5}{:^5}{:^5}{:^20}'.format(i['ho_ten'],i['toan'],i['ly'],i['hoa'],i['tong']))    

ketqua=[]
n= int(input('nhập số sinh viên:'))
obj = [i for i in range(0,n)]
objs =[]
thongtin =[]
total=[]
for i in range(0,n):
    obj[i] = TS('',0,0,0)
    obj[i].thongtin(ketqua)
    obj[i].total()
    objs.append(obj[i])
    thongtin.append(obj[i].thongtin(ketqua))
    total.append(obj[i].total())
TS.out()

    

