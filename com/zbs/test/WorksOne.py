if __name__ == '__main__':
    strr=input("请输入一个年份(20180105)")
    year=strr[0:4]
    moth=strr[4:6]
    day = strr[6:]
    year=int(year)
    moth = int(moth)
    day = int(day)
    evn=[1,3,5,7,8,10,12]
   # if year%4==0 and year%100!=0 and year % 400==0:
    days=0
    for i in range(1,moth+1):
        if i!=moth:
            if str(evn).find(str(i))!=-1:
                days+=31
            else:
                 days+=30
        else:
            days+=day

    if moth>2 :
        print("大于二月")
        if (year % 4 == 0 and year % 100 != 0)or year % 400 == 0:
            days-=1
        else:
            days-=2
    print("当前年份：",year,"今日为本年的第:",days,"天")
    print((year % 4 == 0 and year % 100 != 0)or year % 400 == 0 )
    print()