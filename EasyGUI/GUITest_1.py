import easygui as g
import sys

while 1:
    g.msgbox('欢迎进入第一个界面小游戏')
    msg = '请问你希望学习什么呢？'
    title = '小游戏互动'
    choices = ['谈恋爱', '编程', '琴棋书画', '不知道']

    choice = g.choicebox(msg, title, choices)

    g.msgbox('你的选择是：' + str(choice), '结果')

    msg = '你希望重新开始小游戏吗？'
    title = '请选择'

    if g.ccbox(msg, title):
        pass
    else:
        sys.exit(0)
