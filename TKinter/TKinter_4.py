from tkinter import *

root = Tk()

photo = PhotoImage(file = 'TKinter_4.png')
theLabel = Label(root,
                 text = '委屈巴巴',
                 justify = LEFT,
                 image = photo,
                 compound = CENTER,
                 font = ('微软雅黑', 60),
                 fg = 'white')
theLabel.pack()

root.mainloop()
