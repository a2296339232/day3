if __name__ == '__main__':
    alist=[1,2,3,4,5]
    blist=[2,4,5,6,7]
    mdict={str(m):str(n) for m in alist for n in blist}

    aulist=[str(m)+str(n) for m in alist  for n in blist]

    for i in aulist:
        print(isinstance(i,type("a")))
    #字典遍历
    print(mdict)