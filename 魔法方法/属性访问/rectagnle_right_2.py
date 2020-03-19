class Rectangle():
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            self.__dict__[name] = value

    def getArea(self):
        return self.width * self.height

#更改字典值
#>>>a = Rectangle(4, 5)
#>>>a.getArea()
#20
#a.__dict__
#{'width': 4, 'height': 5}
#>>> a.__dict__['width']
#4
