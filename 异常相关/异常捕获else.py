try:
    int ('abc')     #或者int ('123'),会有两种不同的结果
except ValueError as reason:
    print('出错了！' + str(reason))
else:
    print('没有任何问题')
