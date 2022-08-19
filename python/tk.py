from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("hello")
canvas.pack()

canvas.create_rectangle(10, 10, 100, 100, fill="yellow")
canvas.create_oval(100, 100, 200, 300)

canvas.mainloop()
