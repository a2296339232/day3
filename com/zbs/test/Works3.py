import  random
if __name__ == '__main__':
    mlist=[i for i in range(0,random.choice(range(0,100)))]
    num=random.choice(range(0,100))
    print(num)
    print(mlist)
    if str(mlist).find(str(num))!=-1:
        print("该数字存在数列之中",num)
    else:
        print("该数字不存在数列中")