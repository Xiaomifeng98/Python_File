from tkinter import *

def callback():
    var.set('我信你个鬼，你个糟老头子坏得很')

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('您所下载的影片含有未成年人限制内容，\n请满十八岁以后再点击观看！')

textLabel = Label(root,
                  textvariable = var,
                  justify = LEFT)
textLabel.pack(side = LEFT)

photo = PhotoImage(file = 'TKinter_3.png')
imgLabel = Label(root, image = photo)
imgLabel.pack(side = RIGHT)

theButton = Button(frame2, text = '已满十八周岁', command = callback)
theButton.pack()

frame1.pack(padx = 10, pady = 10)
frame2.pack(padx = 10, pady = 10)

root.mainloop()
