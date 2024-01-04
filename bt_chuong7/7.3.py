import tkinter as tk

window = tk.Tk()

window.title('Bài 7.3 ')

label = tk.Label(window, text="Hello world!", font=("Arial Bold", 50))
label.pack()

label.config(font=("Courier", 30, "bold"), fg="blue")

window.mainloop()