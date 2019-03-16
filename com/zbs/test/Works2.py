if __name__ == '__main__':
    moth1=int(input("请输入男生月份"))
    moth2=int(input("请输入女生月份"))
    mm=moth1+moth2
    if mm % 4 ==0:
        print("有仇")
    elif mm%4==1:
        print("非常有缘")
    elif mm%4==2:
        print("有缘")
    elif mm%4==3:
        print("缘分一般")