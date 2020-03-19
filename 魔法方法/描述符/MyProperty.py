class MyProperty():
    def __init__(self, fget = None, fset = None, fdel = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        print('__get__', instance, owner)
        return self.fget(instance)
    def __set__(self, instance, value):
        print('__set__', instance, value)
        self.fset(instance, value)
    def __delete__(self, instance):
        print('__delete__', instance)
        self.fdel(instance)

class C():
    def __init__(self):
        self._x = None
    def getX(self):
        return self._x
    def setX(self, value):
        self._x = value
    def delX(self):
        del self._x
    x = MyProperty(getX, setX, delX)
#应该是x为MyProperty的一个对象；
#当x被调用时，自动调用__get__
#当x被设置时，自动调用__set__
#当x被删除时，自动调用__delete__
