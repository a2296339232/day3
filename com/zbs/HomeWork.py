if __name__ == '__main__':
    4.
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]
    slist=[]
    chara=""
    for i in klist:
        chara=str(i)
        chara=chara.lstrip()
        chara=chara.rstrip()
        if str(slist).find(chara)==-1:
            slist.append(chara)
    for i in slist:
        print('字符为：',i,"\t",'出现的频率为',str(klist).count(i))

    mdict=dict()
    for i in slist:
        mdict[i]=str(klist).count(i)

    print(mdict)
