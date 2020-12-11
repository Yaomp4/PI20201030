
import random
m=['messi','Neymar','CR7','mbappe','張耀天']
k=['踩','丟','踢','打','傳']
a=['足球','高爾夫球','桌球','羽球','網球']


for sentence in range(10):
    print(random.sample(m,1)[0],random.sample(k,2)[0],random.sample(a,1)[0])
