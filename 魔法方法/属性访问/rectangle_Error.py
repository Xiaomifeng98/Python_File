class Rectangle():
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            #这里会发生错误，给属性设置了值，又会重新调用__setattr__，一直递归，出现问题
            self.name = value

    def getArea(self):
        return self.width * self.height
