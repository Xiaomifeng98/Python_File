class Celsius():
    #初始化摄氏度
    def __init__(self, value = 26.0):
        print('初始化')
        self.value = float(value)

    #当被调用时，返回值
    def __get__(self, instance, owner):
        print('摄氏度__get__', instance, owner)
        return self.value

    #当被赋值时，调用
    def __set__(self, instance, value):
        print('摄氏度__set__', instance, value)
        self.value = float(value)

class Fahrenheit():
    
    #当调用华氏度是，将摄氏度转换过去
    def __get__(self, instance, owner):
        print('华氏度__get__', instance, owner)
        return instance.cel * 1.8 +32
    
    #当设置华氏度的值时，自动转换为摄氏度
    def __set__(self, instance, value):
        print('华氏度__set__', instance, value)
        instance.cel = (float(value) - 32) / 1.8
    
class Temperature():
    cel = Celsius()
    fah = Fahrenheit()
