
n=input('請問你班上有幾位同學?')
n=int(n)
scores=[]

#輸入名字跟分數的清單
for i in range(n):
   c=input('請輸入同學的名字')
   s=int(input('請輸入這位同學的分數'))
   scores.append(c)
   scores.append(s)
print(scores)

#平均數
total=0
for i in range(1,2*n,2):
    total=scores[i]+total
    
average=total/n  
print('平均分數是',average)

# 最大數
biggest=0

for i in range(1,2*n,2):
    if scores[i] > biggest:
        biggest=scores[i]
        biggestone=scores[i-1]
print(biggestone,'得最高分',biggest,'分')
   
# 最小數
smallest=0

for i in range(1,2*n,2):
    if scores[i] < smallest:
        smallest=scores[i]
        smallestone=scores[i-1]
print(smallestone,'得最低分',smallest,'分')    



