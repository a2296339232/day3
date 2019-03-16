def jiuJiu():
    for i in range(1,10):
        for j in range(1,i+1):
            print(i,"*",j,"=",i*j,'\t',end="")
        print()

def sanJiao(num):
    for i in range(1, num):
        for j in range(1, num - i):
            print(" ", end="")
        for k in range(1, i + 1):
            print("* ", end="")
        print("")
def shuLie(len):
    mlist=[i for i in range(0,len*10)]
    for i in mlist:
        if(i%10==9 and i!=0):
            print(str(i).ljust(5))
        else:
            print(str(i).ljust(5),end="")
