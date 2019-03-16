if __name__ == '__main__':
    str = input("请输入一个字符串")
    strr=""
    for i in str:
        if str.count(i)>=2:
            if strr.find(i)==-1:
                print("重复的字符为：",i,'\t',"重复次数为",str.count(i))
                strr+=i



