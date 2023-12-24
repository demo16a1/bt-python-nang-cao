#xây dựng lớp phân số
class PS:
    def __init__(self,tuso,mauso):
        self.tuso=mauso
        self.mauso=tuso
    def nhap_ps(self):
        self.tuso=int(input('Tử số:'))
        self.mauso=int(input('Mẫu số:'))

    def kiemtra(self):
        if self.mauso==0 or self.tuso==0:
           print("lỗi,phân số không hợp lệ!!!")
        else:
           print("phân số :{}/{}".format(self.tuso,self.mauso))
        
giatri=PS(0,0)
giatri.nhap_ps()
giatri.kiemtra()



        