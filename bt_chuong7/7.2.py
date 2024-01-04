import tkinter as tk

# Tạo cửa sổ chính 
window=tk.Tk()

#Thêm tiêu đề cho cửa sổ
window.title('Welcome !!')

#Thêm label
lbl=tk.Label(window,text='Hello world')
lbl.pack()

#Đặt kích thước cửa sổ 
window.geometry('280x60')

#Bắt đầu vòng lặp chạy ứng dụng
window.mainloop()