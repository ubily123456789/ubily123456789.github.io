from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("hello")
canvas.pack()

canvas.create_rectangle(200, 10, 100, 100, fill="yellow")
canvas.create_oval(100, 100, 200, 300, fill="black")
canvas.create_polygon(10, 10, 100, 100, 0, 100, fill="blue")

canvas.mainloop()
