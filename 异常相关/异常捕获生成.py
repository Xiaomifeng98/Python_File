#如果程序出错，try内的语句不会再继续运行
try:
    #int('abc')          #错误，ValueError
    #sum = 1 + '1'   #错误
    f = open('异常捕获生成测试文档.txt', 'w')
    print(f.write('This is the error catch test word. You can delete this document when you no longer use it.'))
    f.close()
except OSError as reason:
    print('文件出错！出错的原因是：' + str(reason))
except TypeError as reason:
    print('类型出错！错误的原因是：' + str(reason))
    #或者是用except(OSError, TypeError)#
except:                 #其他错误（错误数大于等于0，上面的可以不要，但是不推荐）
    print('出错啦')
finally:
    f.close()

raise OSError('系统故障引起中断')
