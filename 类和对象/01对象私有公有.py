class Person:
    #私有成员不能通过.访问，只能由内部函数访问，但是可以通过_类名__变量名访问私有成员
    __name = '私有名字'
    name = '公有名字'        #公有成员可以直接访问
    def get_name(self):
        print(self.__name)
