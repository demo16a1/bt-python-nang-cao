import tkinter as tk
class Bai7_4:
    def __init__(self, root):
        self.root = root
        self.root.title("Thông tin sinh viên")
        self.root.geometry('350x100')
        self.lbl1 = tk.Label(root, text="Tên sinh viên:") 
        self.lbl1.grid(column=0, row=0)
        self.txt1 = tk.Entry(root, width=20)
        self.txt1.grid(column=1, row=0)
        self.txt1.focus()

        self.lbl2 = tk.Label(root, text="ID sinh viên:")
        self.lbl2.grid(column=0, row=2)
        self.txt2 = tk.Entry(root, width=20)
        self.txt2.grid(column=1, row=2)
        self.txt2.focus()

        self.lbl3 = tk.Label(root, text="Mật khẩu:") 
        self.lbl3.grid(column=0, row=3)
        self.txt3 = tk.Entry(root, width=20,show='*')
        self.txt3.grid(column=1, row=3)
        self.txt3.focus()
        
        self.submit_button = tk.Button(self.root, text="Gửi",command=self.submit)
        self.submit_button.grid(column=0,row=8)
    def submit(self):
        print('Tên sinh viên:',self.txt1.get())
        print('ID sinh viên:',self.txt2.get())
        print('Mật khẩu:',self.txt3.get())
    
         
if __name__ == "__main__":
    root = tk.Tk()
    app = Bai7_4(root)
    root.mainloop() 