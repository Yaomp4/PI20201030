
import random
num=random.randint(0,20)
i=0
while i<5:
    guess=input('請輸入1-20其中一個數')
    guess=int(guess)
    i=i+1
    if num<guess:
        print('小一點！')
    elif num>guess:
        print('大一點')
    else:
        print('你中獎了 你猜了',i,'次')
    
        
    