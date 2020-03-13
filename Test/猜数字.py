import random
times = 3
secret = random.randint(1, 10)
print('-------------------------------------')
guess = 0
print('猜一下我想的数字？')
while(guess != secret) and (times > 0):
    temp = input()
    guess = int(temp)
    times = times - 1
    if guess == secret:
        print('真厉害')
    else:
        if guess > secret:
            print('大了大了')
        else:
            print('小了小了')
        if times > 0:
            print('还有', times, '次机会')
        else:
            print('没有机会了')
print('游戏结束')
