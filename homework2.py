math=input("請輸入妳數學的成績")
eng=input("請輸入你英文的成績")
math=int(math)
eng=int(eng)
if math>=90 and eng>=90:
    print('有獎品')
elif math>=90 and eng<90:
    print('再加油')
elif math<90 and eng>=90:
    print('再加油')
elif math<90 and eng<90:
    print('要處罰')
else:
    print('請輸入0-100的數')
    