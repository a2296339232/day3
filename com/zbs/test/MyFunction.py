if __name__ == '__main__':
    def mySer(name):
        if name=='木吉':
         print("吼吼吼吼全给党")

        if name=="贝奥兰迪" :
            print("come wes go！")


    mySer("木吉")

    def mySer1(name):
        if name=='木吉':
         return "吼吼吼吼全给党"

        if name=="贝奥兰迪" :
            return "come wes go！"
        else:
            return "no"


    print(mySer1("贝奥兰迪"))
    print(mySer1(1))