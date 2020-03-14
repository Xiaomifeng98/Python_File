import cv2
import shutil
import os
import easygui as g

g.msgbox('请选择需要美颜的照片')
f_open_way = g.fileopenbox(default = '*', filetypes = [['.png', 'PNG files'], ['.jpg', 'JPG files']])
if os.path.exists('D:\\Temp'):
    pass
else:
    os.mkdir('D:\\Temp')
temp_open = 'D:\\Temp\\temp_old.png'
temp_save = 'D:\\Temp\\temp_new.png'

if(f_open_way == None):
    exit(0)
else:
    shutil.copyfile(f_open_way, temp_open)
    value = int(g.integerbox(title = '美颜程度', msg = '请输入从0到100的数字，数值越大，美颜程度越高', lowerbound =0, upperbound = 100))
    image = cv2.imread(temp_open)
    image_dst = cv2.bilateralFilter(image, value, value*2, value/2)
    cv2.imwrite(temp_save, image_dst)
    f_save_way = g.filesavebox(msg = '请选择保存的路径', default = 'YouAreSoBeautiful.png', filetypes = [['.png', 'PNG files'], ['.jpg', 'JPG files']])
    shutil.copyfile(temp_save, f_save_way)
    g.msgbox('文件已保存至' + f_save_way)

os.remove(temp_open)
os.remove(temp_save)
os.removedirs('D:\\Temp')
