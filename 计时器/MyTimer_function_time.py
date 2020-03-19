import time as t

class MyTimer():

    def __init__(self, func, number = 1000000):
        self.prompt = 'Timing not started'
        self.lasted = 0.0
        self.default_timer = t.perf_counter
        self.func = func
        self.number = number

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        result = self.lasted + other.lasted
        prompt = 'Total running time is %0.2f seconds.' % result
        return prompt
    
    def timing(self):
        self.begin = self.default_timer()
        for i in range(self.number):
            self.func()
        self.end = self.default_timer()
        self.lasted = self.end - self.begin
        self.prompt = 'Total running time is %0.10f seconds' % self.lasted

    def set_timer(self, timer):
        if timer == 'process_time':
            self.default_timer = t.process_time
        elif timer == 'perf_counter':
            self.default_timer = t.perf_counter
        else:
            print('Invalid input, please input per_counter or process_time')

def test():
    text = 'I love FishC.com'
    char = 'o'
    if char in text:
        pass

t1 = MyTimer(test, 1)
t1.timing()
print(t1)
