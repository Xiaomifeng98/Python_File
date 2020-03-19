import time as t

class MyTimer():

    def __init__(self):
        self.unit = [' year(s)', ' month' , ' day', ' hour', ' minute', ' second.']
        self.borrow = [0, 12, 31, 24, 60, 60]
        self.prompt = 'Timing not started'
        self.lasted = []
        self.start_num = 0
        self.stop_num = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        prompt = 'Total running time is: '
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt
    
    #_________________________________________________________Start the timer
    def start(self):
        self.start_num = t.localtime()
        self.prompt = 'Tips: please call stop() to stop timing.'
        print('Start the timer.')

    #_________________________________________________________Stop the timer
    def stop(self):
        if not self.start_num:
            print('Tips: please call start() to start timing.')
        else:
            self.stop_num = t.localtime()
            self._calc()
            print('Stop the timer.')

    # _________________________________Internal method: calculate running time
    def _calc(self):
        self.lasted = []
        self.prompt = 'Total running time is: '
        for index in range(6):
            temp = self.stop_num[index] - self.start_num[index]
            #If the low is not enough, borrow from the high
            if temp < 0:
                #Test the high position can be borrowed, if not, borrow from the higher position.
                i = 1
                while self.lasted[index - i] < 1:
                    self.lasted[index - i]  += self.borrow[index - i] - 1
                    self.lasted[index - i - 1] -= 1
                    i += 1

                self.lasted.append(self.borrow[index] + temp)
                self.lasted[index - 1] -= 1
            else:
                self.lasted.append(temp)
        #Since the high position will be borrowed at any time, the print should be replaced at the end.
        for index in range(6):
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        #Initialize variables for the next round.
        self.start_num = 0
        self.stop_num = 0