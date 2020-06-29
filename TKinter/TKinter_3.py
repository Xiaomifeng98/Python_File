from tkinter import *

root = Tk()

textLabel = Label(root,
                  text = '您所下载的影片含有未成年人限制内容，\n请满十八岁以后再点击观看！',
                  justify = LEFT,
                  padx = 10)
textLabel.pack(side = LEFT)

photo = PhotoImage(file = 'TKinter_3.png')
imgLabel = Label(root, image = photo)
imgLabel.pack(side = RIGHT)

root.mainloop()
