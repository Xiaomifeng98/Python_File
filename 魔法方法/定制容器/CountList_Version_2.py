#实现获取、设置和删除一个元素的行为
#增加counter(index)方法，返回index参数所指定的元素访问次数
#实现appen()、pop()、remove()、insert()、clear()和reverse()方法（考虑计数器的对应改变）
class CountList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)
            
    def __len__(self):
        return len(self.count)

    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):
        return self.count[key]

    def append(self, value):
        self.count.append(0)
        super().append(value)

    def pop(self, key = -1):
        del self.count[key]
        return super(),pop(key)

    def remove(self, value):
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value)

    #清空列表
    def clear(self):
        self.count.clear()
        super().clear()

    #倒置列表
    def reverse(self):
        self.count.reverse()
        super().reverse()

a = CountList(1, 2, 3, 4, 5)
a.append(55)
a[3]
